select * from public.staging_patient_visits;
select * from public_analytics_schema.fact_revenue;

select * from public_analytics_schema.dim_branches;
select * from public_analytics_schema.doctors;
select * from public_analytics_schema.dim_risk;

delete from production.dim_doctors;
delete from production.dim_branches;
delete from production.dim_patients;
delete from production.dim_risk;
delete from production.fact_revenue;

select * from production.dim_doctors;
select * from production.dim_branches;
select * from production.dim_patients;
select * from production.dim_risk;
select * from production.fact_revenue;


