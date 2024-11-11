import pandas as pd
import psycopg2
from psycopg2 import sql


# Function to extract data from CSV and load it into the PostgreSQL database
def extract_data_to_postgres(csv_file_path, db_config):
    """
    Extracts data from a CSV file and loads it into the PostgreSQL staging table.

    Args:
    - csv_file_path: Path to the CSV file to extract data from.
    - db_config: Dictionary containing database connection details.
    """
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host=db_config['host'],
        dbname=db_config['dbname'],
        user=db_config['user'],
        password=db_config['password'],
        port = db_config['port']
    )
    cursor = conn.cursor()

    # Insert data into the staging table
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO staging_patient_visits (visit_id, patient_id, patient_name, doctor_id, doctor_name,
                                                specialization, visit_date, diagnosis, treatment, cost)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (row['Visit_ID'], row['Patient_ID'], row['Patient_Name'], row['Doctor_ID'], row['Doctor_Name'],
              row['Specialization'], row['Visit_Date'], row['Diagnosis'], row['Treatment'], row['Cost']))

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

    print(f"Data loaded successfully from {csv_file_path} into the staging table.")

db_config = {
    'host': 'localhost',
    'dbname': 'db',
    'user': 'etl',
    'password': 'secret',
    'port' : '5000'
}

extract_data_to_postgres('../rawdata/staging_data.csv', db_config)