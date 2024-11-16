{{ config(
    materialized='table',
    schema='analytics_schema'
) }}

-- Create the fact table for patient visits
with fact_patient_visits as (
    select
        -- Surrogate keys from dimension tables
        {{ dbt_utils.generate_surrogate_key(['doctor', 'hospital_branch']) }} as doctor_id,
        {{ dbt_utils.generate_surrogate_key(['hospital_branch']) }} as branch_id,
        {{ dbt_utils.generate_surrogate_key(['patient_risk_profile']) }} as risk_id,

        -- Natural keys and attributes
        row_id,
        patient_id,
        date_of_admit,
        date_of_discharge,
        department,

        -- Metrics (facts)
        revenue,
        minutes_to_service,
        number_of_patient_visits


    from {{ source('trans', 'staging_patient_visits') }}
)

select
    -- Surrogate keys
    doctor_id,
    branch_id,
    risk_id,

    -- Natural keys
    row_id,
    patient_id,

    -- Dates
    date_of_admit,
    date_of_discharge,

    -- Metrics
    revenue,
    minutes_to_service,
    number_of_patient_visits

from fact_patient_visits