{{config(
    materialized='table',
    schema = 'analytics_schema'
)}}

with dim_doc as (
    select
        distinct doctor_id,
        doctor_name,
        specialization,
        COUNT(DISTINCT visit_id) AS total_visits
    from {{ source('trans', 'staging_patient_visits')}}
    group by doctor_id, doctor_name, specialization
)
select
    doctor_id,
    doctor_name,
    specialization,
    total_visits
from dim_doc