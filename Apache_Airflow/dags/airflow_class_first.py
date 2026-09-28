from datetime import datetime, timedelta

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def print_first():
    print("this is airflow first print statement")


def print_second():
    print("this is airflow second print statement")


with DAG(
    dag_id='airflow_class_first_dag',
    start_date=datetime(2026, 9, 26),
    schedule=None,
    catchup=False,
    tags=['airflow class', 'first dags', 'learning']
):
    task1 = PythonOperator(
        task_id='task1',
        python_callable=print_first,
        retries=2,
        retry_delay=timedelta(minutes=2)
    )

    task2 = PythonOperator(
        task_id='task2',
        python_callable=print_second,
        retries=2,
        retry_delay=timedelta(minutes=2)
    )

    task1 >> task2