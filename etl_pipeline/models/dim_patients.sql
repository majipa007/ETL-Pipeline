{{ config(materialized='table') }}

WITH staging_data AS (
    SELECT
        patient_id,
        patient_name
    FROM {{ ref('staging_patient_visits') }}
)

SELECT
    DISTINCT patient_id,
    patient_name
FROM staging_data