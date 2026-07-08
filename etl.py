import mysql.connector
import logging
from datetime import date
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
from dotenv import load_dotenv
import os
import random

load_dotenv()

SERVICE_ACCOUNT_FILE = r"F:\Downloads\delivery-analytics-gcp-c2bcb1b8a70c.json"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE
)

bq_client = bigquery.Client(
    credentials=credentials,
    project="delivery-analytics-gcp"
)

logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("HOST =", os.getenv("DB_HOST"))
print("USER =", os.getenv("DB_USER"))
print("DATABASE =", os.getenv("DB_NAME"))
print("PASSWORD EXISTS =", os.getenv("DB_PASSWORD") is not None)

def connect_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST").strip(),
        user=os.getenv("DB_USER").strip(),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME").strip(),
        port=3306,
        connection_timeout=10
    )

def load_to_bigquery_batch(data):
    if not data:
        print("No valid records to upload to BigQuery.")
        return

    table_id = "delivery-analytics-gcp.delivery_dataset.fact_deliveries_v2"
    df = pd.DataFrame(data)
    job = bq_client.load_table_from_dataframe(df, table_id)
    job.result()
    print(f"Loaded {len(data)} rows to BigQuery")

def run_etl():
    print("\nETL STARTED")
    logging.info("ETL started")

    conn = None
    cursor = None

    try:
        conn = connect_db()
        cursor = conn.cursor()

        # ---------------- EXTRACT ----------------
        cursor.execute("""
            SELECT id, order_name, source_location, destination_location
            FROM raw_deliveries
            WHERE processed_flag = FALSE
        """)

        rows = cursor.fetchall()
        print("STEP 1: Rows fetched =", len(rows))

        bq_batch = []
        processed_count = 0
        skipped_count = 0
        failed_count = 0

        if not rows:
            print("No new data to process")
            return

        # ---------------- TRANSFORM ----------------
        for row in rows:
            raw_id, order_name, source, destination = row

            try:
                source = int(source)
                destination = int(destination)
            except ValueError:
                skipped_count += 1
                message = (
                    f"Skipping invalid record "
                    f"(ID={raw_id}, Order={order_name}) "
                    f"because source/destination is not numeric."
                )
                print(message)
                logging.warning(message)
                continue

            delivery_duration = abs(destination - source) * 10
            is_delayed = 1 if delivery_duration > 30 else 0
            distance = delivery_duration / 10
            delivery_date = date.today()
            agent_id = random.randint(101,110)

            bq_batch.append({
                "id": raw_id,
                "agent_id": agent_id,
                "delivery_duration": delivery_duration,
                "distance": float(distance),
                "is_delayed": is_delayed,
                "delivery_date": delivery_date
            })

            cursor.execute("SELECT location_name FROM location_lookup WHERE location_id=%s",(source,))
            r = cursor.fetchone()
            source_name = r[0] if r else "Unknown"

            cursor.execute("SELECT location_name FROM location_lookup WHERE location_id=%s",(destination,))
            r = cursor.fetchone()
            destination_name = r[0] if r else "Unknown"

            cursor.execute("""
                INSERT INTO processed_deliveries
                (order_name, source_location, destination_location,
                 source_name, destination_name, status)
                VALUES (%s,%s,%s,%s,%s,%s)
            """,(order_name,source,destination,source_name,destination_name,"pending"))

            cursor.execute("""
                INSERT INTO fact_deliveries
                (agent_id, delivery_duration, distance, is_delayed, delivery_date)
                VALUES (%s,%s,%s,%s,%s)
            """,(agent_id,delivery_duration,distance,is_delayed,delivery_date))

            cursor.execute(
                "UPDATE raw_deliveries SET processed_flag=TRUE WHERE id=%s",
                (raw_id,)
            )

            processed_count += 1

        # ---------------- LOAD ----------------
        load_to_bigquery_batch(bq_batch)

        conn.commit()

        print("\n========== ETL SUMMARY ==========")
        print(f"Rows fetched      : {len(rows)}")
        print(f"Rows processed    : {processed_count}")
        print(f"Rows skipped      : {skipped_count}")
        print(f"Rows failed       : {failed_count}")
        print(f"BigQuery uploaded : {len(bq_batch)}")
        print("Status            : SUCCESS")
        print("================================")

    except Exception as e:
        failed_count = failed_count + 1 if 'failed_count' in locals() else 1
        if conn:
            conn.rollback()
        logging.exception("ETL failed")
        print("ERROR:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    run_etl()
