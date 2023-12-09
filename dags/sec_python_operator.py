from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args={
    'owner':'anhnt',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}

def greet():
    print("hello {name} ")

with DAG(
    dag_id = 'second_dag',
    default_args = default_args,
    description ='This is my python dag',
    start_date =datetime(2023,12,10),
    schedule_interval = '@daily'
) as dag:
    task1= PythonOperator(
        task_id = 'greet',
        python_callable = greet,
        op_kwargs = {'name':'anhnt'}
    )

    task1  

