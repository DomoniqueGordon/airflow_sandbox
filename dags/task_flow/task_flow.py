from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

import logging


default_args = {"start_date": days_ago(1)}


@dag(schedule_interval="@daily", default_args=default_args, catchup=False)
def task_flow():
    @task
    def extract_data():
        return {"name": "Dom", "age": 29, "occupation": "Data Engineer"}

    @task(multiple_outputs=True)
    def transform_data(response):
        logging.info(response)
        response.update({"hobby": "Working out"})
        return response

    @task
    def load_data(data):
        logging.info(data)

    load_data(transform_data(extract_data()))


dag = task_flow()
