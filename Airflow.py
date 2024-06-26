from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
default_args = {
    'owner':'Jortilles',
    'retries':5,
    'retry_delay':timedelta(minutes=1)
}
with DAG(
    dag_id='a_simple_dag_jortilles',
    description='Esto es una descripción',
    default_args=default_args,
    start_date=datetime(2022,1,1,1),
    schedule_interval='@daily'
) as dag: 
    tarea_A = BashOperator(
        task_id ='primera_tarea',
        bash_command = 'echo "hello world"'
    ) 
    tarea_B = BashOperator(
        task_id ='segunda_tarea',
        bash_command = 'echo "existo"'
    )
    tarea_C = BashOperator(
        task_id ='tercera_tarea',
        bash_command = 'echo "pero no tanto"'
    )
    tarea_D = BashOperator(
        task_id ='cuarta_tarea',
        bash_command = 'echo "Adios"'
    )
    tarea_A >> [tarea_B, tarea_C] >> tarea_D
