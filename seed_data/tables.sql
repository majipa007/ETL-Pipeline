SET SEARCH_PATH TO public;


-- Staging Table: This is where we initially load our raw data (from CSV).
CREATE TABLE staging_patient_visits (
    visit_id SERIAL PRIMARY KEY,
    patient_id INT,
    patient_name VARCHAR(255),
    doctor_id INT,
    doctor_name VARCHAR(255),
    specialization VARCHAR(100),
    visit_date DATE,
    diagnosis TEXT,
    treatment TEXT,
    cost DECIMAL
);

-- Patient Dimension Table: Stores unique patient information.
CREATE TABLE patient_dim (
    patient_id INT PRIMARY KEY,
    patient_name VARCHAR(255)
);

-- Doctor Dimension Table: Stores unique doctor information.
CREATE TABLE doctor_dim (
    doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(255),
    specialization VARCHAR(100)
);

-- Visit Fact Table: Stores the details of each hospital visit, linking patient and doctor.
CREATE TABLE visit_fact (
    visit_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    visit_date DATE,
    diagnosis TEXT,
    treatment TEXT,
    cost DECIMAL
);



