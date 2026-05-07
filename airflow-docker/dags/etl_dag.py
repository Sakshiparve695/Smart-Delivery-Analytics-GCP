from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

# Docker path
sys.path.append("/opt/project")

from etl import run_etl

default_args = {
    'owner': 'sakshi',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='delivery_etl_pipeline',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='*/2 * * * *',
    catchup=False
) as dag:

    run_etl_task = PythonOperator(
        task_id='run_etl',
        python_callable=run_etl
    )

    run_etl_task