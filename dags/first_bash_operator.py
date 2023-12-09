from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    'owner':'anhnt',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id = 'our_first_dag',
    default_args = default_args,
    description ='This is my first dag',
    start_date =datetime(2023,12,9,2),
    schedule_interval = '@daily'
) as dag:
    task1= BashOperator(
        task_id ='task11',
        bash_command = 'echo who read this is a dawg'
    )

    task1
