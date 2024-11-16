{{ config(
    materialized='table',
    schema='analytics_schema'
) }}

-- Create the patient risk dimension table in the analytics_schema
with dim_risk as (
    select
        {{ dbt_utils.generate_surrogate_key(['patient_risk_profile']) }} as risk_id,
        patient_risk_profile,  -- Ensure this column exists in the source table
        department,
        count(*) as cases,
        sum(revenue) as revenue
    from {{ source('trans', 'staging_patient_visits') }}
    group by patient_risk_profile, department
)
select
    risk_id,
    patient_risk_profile,
    department,
    revenue
from dim_risk
