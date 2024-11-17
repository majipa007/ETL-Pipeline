{{ config(
    materialized='table',
    schema='analytics_schema'
) }}

-- Create the doctors dimension table in the analytics_schema
with dim_doc as (
    select
        {{ dbt_utils.generate_surrogate_key(['doctor', 'department']) }} as doctor_id,
        doctor,
        department,
        count(*) as total_visits,
        sum(revenue) as revenue
    from {{ source('trans', 'staging_patient_visits') }}
    group by doctor_id, doctor, department
)
select
    doctor_id,
    doctor,
    department,
    total_visits,
    revenue
from dim_doc
