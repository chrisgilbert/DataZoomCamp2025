-- Get the highest paying districts for the day

SELECT 
  sum(t.total_amount) as sum_total,
  z."Zone",
  lpep_pickup_datetime::date as date
FROM public.green_taxi_trips t
  join taxi_zones z
  on (t."PULocationID" = z."LocationID")
where 
  lpep_pickup_datetime::date in ('2019-10-18')
group by z."Zone", lpep_pickup_datetime::date
order by sum_total desc 
