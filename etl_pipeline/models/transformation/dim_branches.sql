{{ config(
    materialized='table',
    schema='analytics_schema'
) }}

-- Create the doctors dimension table in the analytics_schema
with dim_bra as (
    select
        {{ dbt_utils.generate_surrogate_key(['hospital_branch']) }} as branch_id,
        hospital_branch,
        sum(revenue) as revenue
    from {{ source('trans', 'staging_patient_visits') }}
    group by branch_id, hospital_branch
)
select
    branch_id,
    hospital_branch,
    revenue
from dim_bra