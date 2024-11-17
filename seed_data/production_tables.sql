CREATE SCHEMA IF NOT EXISTS production;

-- Fact Table
CREATE TABLE IF NOT EXISTS production.fact_patient_visits (
    doctor_id VARCHAR,
    branch_id VARCHAR,
    risk_id VARCHAR,
    row_id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    minutes_to_service INTEGER,
    number_of_patient_visits INTEGER,
    revenue NUMERIC(10, 2)
);

-- Dimension Tables
CREATE TABLE IF NOT EXISTS production.dim_doctors (
    doctor_id VARCHAR PRIMARY KEY,
    doctor VARCHAR(255),
    department VARCHAR(255),
    total_visits INTEGER,
    revenue NUMERIC(10, 2)
);

CREATE TABLE IF NOT EXISTS production.dim_branches (
    branch_id VARCHAR PRIMARY KEY,
    hospital_branch VARCHAR(255),
    department VARCHAR(255),
    revenue NUMERIC(10, 2)
);

CREATE TABLE IF NOT EXISTS production.dim_risk (
    risk_id VARCHAR PRIMARY KEY,
    patient_risk_profile VARCHAR(50),
    department VARCHAR(255),
    revenue NUMERIC(10, 2)
);

CREATE TABLE IF NOT EXISTS production.dim_patients (
    patient_id INTEGER PRIMARY KEY,
    patient_name VARCHAR(255),
    total_visits INTEGER,
    total_spent NUMERIC(10, 2)
);
