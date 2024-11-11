{{ config(materialized='table') }}

with staging_data as (
    select
        visit_id,
        patient_id,
        doctor_id,
        visit_date,
        diagnosis,
        treatment,
        cost
    FROM {{ ref('staging_patient_visits') }}
)
SELECT
    patient_id,
    doctor_id,
    COUNT(visit_id) AS visit_count,
    SUM(cost) AS total_cost,
    MIN(visit_date) AS first_visit_date,
    MAX(visit_date) AS last_visit_date
FROM staging_data
GROUP BY
    patient_id,
    doctor_id