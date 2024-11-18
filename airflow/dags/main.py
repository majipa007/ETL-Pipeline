from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
}

with DAG(
        dag_id='etl_pipeline_dag',
        default_args=default_args,
        description='ETL pipeline using dbt and Airflow',
        schedule_interval='@daily',
        start_date=days_ago(1),
        catchup=False,
        tags=['etl', 'dbt'],
) as dag:
    # Debug task to check environment
    check_environment = BashOperator(
        task_id='check_environment',
        bash_command='''
            echo "Current working directory: $PWD" &&
            echo "DBT_PROFILES_DIR: $DBT_PROFILES_DIR" &&
            echo "Listing dbt project directory:" &&
            ls -la /opt/airflow/etl_pipeline &&
            echo "DBT version:" &&
            dbt --version
        '''
    )

    # DBT debug task
    dbt_debug = BashOperator(
        task_id='dbt_debug',
        bash_command='cd /opt/airflow/etl_pipeline && dbt debug --config-dir'
    )

    # Modified dbt run task with verbose output
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='''
            cd /opt/airflow/etl_pipeline && \
            echo "Running dbt with profiles.yml in: $DBT_PROFILES_DIR" && \
            dbt run --debug --profiles-dir /opt/airflow/etl_pipeline
        ''',
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /opt/airflow/etl_pipeline && dbt test --profiles-dir /opt/airflow/etl_pipeline'
    )

    success_message = BashOperator(
        task_id='success_notification',
        bash_command='echo "ETL Pipeline completed successfully!"'
    )

    # Updated task dependencies
    check_environment >> dbt_debug >> dbt_run >> dbt_test >> success_message