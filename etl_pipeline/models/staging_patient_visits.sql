{{ config(materialized='table') }}

SELECT *
FROM public.staging_patient_visits
