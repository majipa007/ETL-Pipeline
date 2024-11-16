select * from public_analytics_schema.dim_patients;
select * from public_analytics_schema.dim_doctors;

select * from public.staging_patient_visits order by row_id;

DROP TABLE public_analytics_schema.dim_doctors;
DROP TABLE public_analytics_schema.dim_patients;

select doctor, department, count(*) as assignments 
from public.staging_patient_visits
group by doctor, department
order by assignments Desc;


select doctor, department, count(*)  as assignments, sum(revenue) as revenue 
from public.staging_patient_visits
group by doctor, department
order by doctor;

select count(Distinct doctor)
from public.staging_patient_visits;
