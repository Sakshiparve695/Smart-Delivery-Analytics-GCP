import mysql.connector
import logging
import time
from datetime import date
from google.cloud import bigquery
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# ---------------- BIGQUERY CLIENT ----------------
bq_client = bigquery.Client()

# ---------------- LOGGING ----------------
logging.basicConfig(
    filename='etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------------- DB CONNECTION ----------------
def connect_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# ---------------- BIGQUERY LOAD ----------------
def load_to_bigquery_batch(data):
    table_id = "delivery-analytics-gcp.delivery_dataset.fact_deliveries_v2"

    df = pd.DataFrame(data)

    job = bq_client.load_table_from_dataframe(df, table_id)
    job.result()

    print(f" Loaded {len(data)} rows to BigQuery")

# ---------------- ETL FUNCTION ----------------
def run_etl():
    print("\n ETL STARTED")
    logging.info("ETL started")

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

        if not rows:
            print(" No new data to process")
            return

        # ---------------- PREPARE BATCH ----------------
        bq_batch = []

        # ---------------- PROCESS ----------------
        for row in rows:
            raw_id, order_name, source, destination = row

            source = int(source)
            destination = int(destination)

            # -------- TRANSFORM --------
            delivery_duration = abs(destination - source) * 10
            is_delayed = 1 if delivery_duration > 30 else 0
            distance = delivery_duration / 10
            delivery_date = date.today()

            print("PROCESSING:", order_name, delivery_duration, is_delayed)

            # -------- ADD TO BIGQUERY BATCH --------
            bq_batch.append({
                "id": raw_id,
                "agent_id": 1,
                "delivery_duration": delivery_duration,
                "distance": float(distance),
                "is_delayed": is_delayed,
                "delivery_date": delivery_date
            })

            # -------- LOOKUP --------
            cursor.execute(
                "SELECT location_name FROM location_lookup WHERE location_id = %s",
                (source,)
            )
            result = cursor.fetchone()
            source_name = result[0] if result else "Unknown"

            cursor.execute(
                "SELECT location_name FROM location_lookup WHERE location_id = %s",
                (destination,)
            )
            result = cursor.fetchone()
            destination_name = result[0] if result else "Unknown"

            # -------- INSERT PROCESSED --------
            cursor.execute("""
                INSERT INTO processed_deliveries 
                (order_name, source_location, destination_location, source_name, destination_name, status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (order_name, source, destination, source_name, destination_name, "pending"))

            # -------- INSERT FACT (MYSQL BACKUP) --------
            cursor.execute("""
                INSERT INTO fact_deliveries 
                (agent_id, delivery_duration, distance, is_delayed, delivery_date)
                VALUES (%s, %s, %s, %s, %s)
            """, (1, delivery_duration, distance, is_delayed, delivery_date))

            # -------- MARK PROCESSED --------
            cursor.execute("""
                UPDATE raw_deliveries
                SET processed_flag = TRUE
                WHERE id = %s
            """, (raw_id,))

        # ---------------- LOAD TO BIGQUERY (BATCH) ----------------
        load_to_bigquery_batch(bq_batch)

        conn.commit()
        conn.close()

        print(" ETL COMPLETED")
        logging.info(f"Processed {len(rows)} records successfully")

    except Exception as e:
        logging.error(f"ETL failed: {str(e)}")
        print(" ERROR:", str(e))

# ---------------- AUTO RUN ----------------
#if __name__ == "__main__":
    #while True:
        #run_etl()
        #print(" Waiting 60 seconds...\n")
        #time.sleep(60)