{{
    config(materialized = "table",
    schema = "analytics_schema")
}}

SELECT DISTINCT
    doctor_id,
    doctor_name,
    specialization
FROM {{ source('staging_data', 'staging_patient_visits') }}