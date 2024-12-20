{{ config(
    materialized='table',
    schema='analytics_schema'
) }}

-- Create the patients dimension table in the analytics_schema
with dim_pat as (
    select
        patient_id,
        patient_name,
        count(*) as total_visits,
        sum(revenue) as total_spent
    from {{ source('trans', 'staging_patient_visits') }}
    group by patient_id, patient_name
)
select
    patient_id,
    patient_name,
    total_visits,
    total_spent
from dim_pat
