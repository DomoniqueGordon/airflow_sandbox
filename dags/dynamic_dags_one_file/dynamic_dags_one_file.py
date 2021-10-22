from airflow import DAG
from airflow.decorators import task

from datetime import datetime

tables = {
    "products": {
        "schedule_interval": "@weekly",
        "columns": ["product", "price", "location"],
        "process_table": "manufactured_products",
        "store_table": "available_products",
    },
    "customers": {
        "schedule_interval": "@daily",
        "columns": ["customer", "email", "address"],
        "process_table": "stat_customers",
        "store_table": "raw_customers",
    },
}


def generate_dag(dag_id, start_date, schedule_interval, details):
    with DAG(
        dag_id, start_date=start_date, schedule_interval=schedule_interval
    ) as dag:

        @task
        def extract():
            print(f"Extract columns {details['columns']}")

        @task
        def process():
            print(f"Process table {details['process_table']}")

        @task
        def store():
            print(f"Store table {details['store_table']}")

        extract() >> process() >> store()

    return dag


for table, details in tables.items():
    dag_id = f"dynamic_dag_one_file.{table}"
    globals()[dag_id] = generate_dag(
        dag_id, datetime(2021, 1, 1), details["schedule_interval"], details
    )
