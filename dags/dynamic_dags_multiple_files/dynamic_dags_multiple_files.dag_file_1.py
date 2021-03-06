from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {"start_date": datetime(2021, 1, 1)}

dag = DAG(
    "dynamic_dag_multiple_files.dag_file_1",
    schedule_interval="@daily",
    default_args=default_args,
)

with dag:
    extract_data = DummyOperator(task_id="extract-data")
    transform_data = DummyOperator(task_id="transform-data")
    load_data = DummyOperator(task_id="load-data")
