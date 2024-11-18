CREATE TABLE staging_patient_visits (
    row_id INT PRIMARY KEY,
    date_of_admit DATE,
    date_of_discharge DATE,
    doctor VARCHAR(255),
    hospital_branch VARCHAR(255),
    department_type VARCHAR(255),
    department VARCHAR(255),
    patient_id INT,
    patient_name VARCHAR(255),
    patient_risk_profile VARCHAR(255),
    revenue FLOAT,
    minutes_to_service INT,
    number_of_patient_visits INT
);

