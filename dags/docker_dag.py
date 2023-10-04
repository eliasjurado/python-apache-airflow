from airflow.decorators import task, dag
from airflow.providers.docker.operators.docker import DockerOperator

from datetime import datetime

@dag(start_date=datetime(2021,1,1), schedule_interval='@daily',catchup=False)
def docker_dag():

    @task()
    def t1():
        pass

    t2 = DockerOperator(
        task_id='t2',
        container_name='task_t2',
        image='python:3.8-slim-buster',
        command='echo "command running in the docker container"',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        xcom_all=True,
        retrieve_output=True,
        retrieve_output_path='/tmp/script.out',
        mount_tmp_dir=False,
        mem_limit='512m',
        auto_remove=True
    )

    t1() >> t2

dag = docker_dag()