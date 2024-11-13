-- having staging_patient as table as it is temporary and has no updates
{{config (materialized = 'table')}}

-- loading the data extracted from the csv file

SELECT *
FROM {{ source('staging_data', 'staging_patient_visits') }}