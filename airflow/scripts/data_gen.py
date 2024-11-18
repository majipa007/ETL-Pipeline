import pandas as pd
import random
from faker import Faker

# Initialize Faker to generate random names and other info
fake = Faker()

# Function to generate dummy data with unique IDs
def generate_hospital_data(num_records=1000):
    data = []
    start_visit_id = 1000

    # Generate unique IDs for patients
    unique_patient_ids = random.sample(range(1000, 1000 + num_records), num_records)  # Generate unique patient IDs
    # Generate a smaller unique set of doctor IDs
    unique_doctor_ids = list(range(200, 300))  # Limited doctor IDs (to repeat some for multiple visits)

    # Generate unique doctor names based on their IDs
    doctor_info = {doc_id: fake.name() for doc_id in unique_doctor_ids}

    for i in range(num_records):
        visit_id = start_visit_id + i  # Unique visit ID
        patient_id = unique_patient_ids[i]  # Unique patient ID for each record
        patient_name = fake.name()

        # Select a random doctor ID and retrieve consistent doctor info
        doctor_id = random.choice(unique_doctor_ids)
        doctor_name = doctor_info[doctor_id]

        specialization = random.choice(
            ['Cardiology', 'Neurology', 'Orthopedics', 'General Surgery', 'Endocrinology', 'Pediatrics', 'Dermatology']
        )
        visit_date = fake.date_this_year()
        diagnosis = random.choice(
            ['Heart Attack', 'Migraine', 'Broken Leg', 'Appendicitis', 'Diabetes', 'Asthma', 'Knee Pain', 'Skin Rash',
             'Chest Pain', 'Seizures']
        )
        treatment = random.choice(
            ['Angioplasty', 'Medication', 'Casting', 'Appendectomy', 'Insulin Therapy', 'Inhalers', 'Physical Therapy',
             'Topical Cream', 'ECG and Angiogram']
        )
        cost = round(random.uniform(100, 5000), 2)

        data.append([
            visit_id, patient_id, patient_name, doctor_id, doctor_name, specialization,
            visit_date, diagnosis, treatment, cost
        ])

    # Create a DataFrame
    columns = [
        'Visit_ID', 'Patient_ID', 'Patient_Name', 'Doctor_ID', 'Doctor_Name',
        'Specialization', 'Visit_Date', 'Diagnosis', 'Treatment', 'Cost'
    ]
    df = pd.DataFrame(data, columns=columns)

    # Save to CSV file
    df.to_csv('../rawdata/staging_data.csv', index=False)

    print(f"Generated {num_records} rows of dummy data and saved to 'staging_data.csv'.")

# Generate and save the data
generate_hospital_data()