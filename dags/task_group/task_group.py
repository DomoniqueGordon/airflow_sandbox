from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.task_group import TaskGroup
from airflow.utils.dates import days_ago


default_args = {"start_date": days_ago(1)}

with DAG(
    "task_group",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
) as dag:
    extract_data = DummyOperator(task_id="extract-data")

    with TaskGroup("transform-data") as transform_data:
        for item in ["A", "B", "C"]:
            command = f"echo 'Transformation success: {item}"
            BashOperator(task_id=f"transforming-{item}", bash_command="echo")

    load_data = DummyOperator(task_id="load-data")

    extract_data >> transform_data >> load_data
