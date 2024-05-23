from cmath import log
from dateutil import parser
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from dateutil import parser
from airflow.utils import timezone
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'cdpuser1',
    'retry_delay': timedelta(seconds=5),
    'depends_on_past': False,
}

example_dag = DAG(
    'bashoperator-parameter-job',
    default_args=default_args,
    start_date=parser.isoparse("2020-11-11T20:20:04.268Z").replace(tzinfo=timezone.utc),
    schedule_interval='@once',
    is_paused_upon_creation=False
)

task_1 = BashOperator(
    task_id="parameterized_task",
    bash_command="echo Good Morning All!",
    dag=example_dag,
)

task_1
