FROM ${AIRFLOW_IMAGE_NAME:-apache/airflow:latest-python3.8}

USER airflow

ENV PYTHONPATH "${PYTHONPATH}:/sandbox/"

