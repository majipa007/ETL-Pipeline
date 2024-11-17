from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

# Default args for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define DAG
with DAG(
    dag_id='etl_pipeline_dag',
    default_args=default_args,
    description='An ETL pipeline that extracts, transforms, and loads data using dbt and Airflow',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['etl', 'dbt'],
) as dag:
    # Task 4: End of the DAG - Success notification (optional)
    start_message = BashOperator(
        task_id='start_message',
        bash_command='echo "ETL Pipeline started successfully!"'
    )

    # # Task 1: Transform data using dbt run
    # dbt_run = BashOperator(
    #     task_id='dbt_run',
    #     bash_command='cd /opt/airflow/dbt_project && dbt run'
    # )

    # Task 2: Test dbt models to ensure they are working correctly
    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /opt/airflow/dbt_project && dbt test'
    )

    # Task 3: PostgresOperator to validate data in production tables
    validate_production = PostgresOperator(
        task_id='validate_production',
        postgres_conn_id='postgres_default',  # Connection ID defined in Airflow
        sql='''
        SELECT COUNT(*) AS record_count 
        FROM analytics_schema.fact_patient_visits 
        WHERE revenue IS NOT NULL;
        '''
    )

    # Task 4: End of the DAG - Success notification (optional)
    success_message = BashOperator(
        task_id='success_notification',
        bash_command='echo "ETL Pipeline completed successfully!"'
    )

    # Define task dependencies
    start_message >> dbt_test >> validate_production >> success_message
