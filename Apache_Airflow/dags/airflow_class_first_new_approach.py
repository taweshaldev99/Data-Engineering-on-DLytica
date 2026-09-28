from datetime import datetime, timedelta
from airflow.sdk import dag, task


@dag(
    dag_id='airflow_first_class_new_approach_dag2',
    start_date=datetime(2026, 9, 26),
    schedule=None,
    catchup=False,
    tags=['new approach', 'first dags', 'learning']
)
def first_dag_decorator():
    @task.python(task_id="task1")
    def print_first():
        print('this is new approach dag implementation')

    @task.python(task_id="task2")
    def print_second():
        print('this is new second function implementation')

    task1 = print_first()
    task2 = print_second()
    task1 >> task2


first_dag_decorator()