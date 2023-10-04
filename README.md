# python-apache-airflow

Programming tasks for data processing using Python and Apache-Airflow with support from Docker, Linux, Postgres, Redis and ElasticSearch.

## Apache Airflow

- Airflow is an orchestrator, not a processing framework. Process your gigabytes of data outside of Airflow (i.e. You have a Spark cluster, you use an operator to execute a Spark job, and the data is processed in Spark).

- A DAG is a data pipeline, an Operator is a task.

- An Executor defines how your tasks are executed, whereas a worker is a process executing your task

- The Scheduler schedules your tasks, the web server serves the UI, and the database stores the metadata of Airflow.


## Dataset limitations

- DAGs can only use Datasets in the same Airflow instance. A DAG cannot wait for a Dataset defined in another Airflow instance.

- Consumer DAGs are triggered every time a task that updates datasets completes successfully. Airflow doesn't check whether the data has been effectively updated.

- You can't combine different schedules like datasets with cron expressions.

- If two tasks update the same dataset, as soon as one is done, that triggers the Consumer DAG immediately without waiting for the second task to complete.

- Airflow monitors datasets only within the context of DAGs and Tasks. If an external tool updates the actual data represented by a Dataset, Airflow has no way of knowing that.