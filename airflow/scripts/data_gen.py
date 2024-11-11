import pandas as pd
import random
from faker import Faker

# Initialize Faker to generate random names and other info
fake = Faker()


# Function to generate 1000 rows of dummy data
def generate_hospital_data(num_records=1000):
    data = []
    for i in range(1, num_records + 1):
        visit_id = i
        patient_id = random.randint(100, 999)
        patient_name = fake.name()
        doctor_id = random.randint(200, 299)
        doctor_name = fake.name()
        specialization = random.choice(
            ['Cardiology', 'Neurology', 'Orthopedics', 'General Surgery', 'Endocrinology', 'Pediatrics', 'Dermatology'])
        visit_date = fake.date_this_year()
        diagnosis = random.choice(
            ['Heart Attack', 'Migraine', 'Broken Leg', 'Appendicitis', 'Diabetes', 'Asthma', 'Knee Pain', 'Skin Rash',
             'Chest Pain', 'Seizures'])
        treatment = random.choice(
            ['Angioplasty', 'Medication', 'Casting', 'Appendectomy', 'Insulin Therapy', 'Inhalers', 'Physical Therapy',
             'Topical Cream', 'ECG and Angiogram'])
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

    print("Generated 1000 rows of dummy data and saved to 'hospital_visits.csv'.")


# Generate and save the data
generate_hospital_data()
