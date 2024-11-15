import pandas as pd
import psycopg2

def extract_data_to_postgres(csv_file_path, db_config):
    """
    Extracts data from a CSV file and loads it into the PostgreSQL staging table.

    Args:
    - csv_file_path: Path to the CSV file to extract data from.
    - db_config: Dictionary containing database connection details.
    """
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Convert date columns to pandas datetime format (ensure proper format)
    df['Date of Admit'] = pd.to_datetime(df['Date of Admit'], format='%m/%d/%Y', errors='raise')
    df['Date of Discharge'] = pd.to_datetime(df['Date of Discharge'], format='%m/%d/%Y', errors='raise')

    # Log missing discharge dates
    missing_discharge_count = df['Date of Discharge'].isna().sum()
    print(f"Number of missing discharge dates: {missing_discharge_count}")

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host=db_config['host'],
        dbname=db_config['dbname'],
        user=db_config['user'],
        password=db_config['password'],
        port=db_config['port']
    )
    cursor = conn.cursor()

    # Insert data into the staging table
    for _, row in df.iterrows():
        date_of_admit = row['Date of Admit'] if not pd.isna(row['Date of Admit']) else None
        date_of_discharge = row['Date of Discharge'] if not pd.isna(row['Date of Discharge']) else None

        cursor.execute("""
            INSERT INTO staging_patient_visits (
                row_id, date_of_admit, date_of_discharge, doctor, hospital_branch, department_type, 
                department, patient_id, patient_name, patient_risk_profile, revenue, minutes_to_service, 
                number_of_patient_visits
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['Row_ID'], date_of_admit, date_of_discharge, row['Doctor'],
            row['Hospital Branch'], row['Department Type'], row['Department'],
            row['Patient ID'], row['Patient Name'], row['Patient Risk Profile'],
            row['Revenue'], row['Minutes to Service'], row['Number of Patient Visits']
        ))

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

    print(f"Data loaded successfully from {csv_file_path} into the staging table.")

# Database connection configuration
db_config = {
    'host': 'localhost',
    'dbname': 'db',
    'user': 'etl',
    'password': 'secret',
    'port': '5000'
}

# Extract data from the CSV and load it into PostgreSQL
extract_data_to_postgres('../rawdata/hospital_data.csv', db_config)