{{ config(materialized='table') }}

WITH staging_data AS (
    SELECT
        doctor_id,
        doctor_name,
        specialization
    FROM {{ ref('staging_patient_visits') }}
)

SELECT
    DISTINCT doctor_id,
    doctor_name,
    specialization
FROM staging_data
