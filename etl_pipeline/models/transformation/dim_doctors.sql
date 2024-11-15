{{ config(
    materialized='table',
    schema='analytics_schema'
) }}

-- Create the doctors dimension table in the analytics_schema
with dim_doc as (
    select
        doctor_id,
        doctor_name,
        specialization,
        count(distinct visit_id) as total_visits
    from {{ source('trans', 'staging_patient_visits') }}
    group by doctor_id, doctor_name, specialization
)
select
    doctor_id,
    doctor_name,
    specialization,
    total_visits
from dim_doc
