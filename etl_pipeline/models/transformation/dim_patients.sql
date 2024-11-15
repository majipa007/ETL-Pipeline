{{config(
    materialized='table',
    schema = 'analytics_schema'
)}}
 -- store in analytics_schema

with dim_pat as (
    select
        patient_id,
        patient_name,
    COUNT(DISTINCT visit_id) AS total_visits
    from {{source('trans', 'staging_patient_visits')}}
    group by patient_id, patient_name
)
select
    patient_id,
    patient_name,
    total_visits
from dim_pat