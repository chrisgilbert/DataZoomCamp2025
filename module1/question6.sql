SELECT 
  max(t.tip_amount) max_tip,
  z."Zone"
FROM 
  public.green_taxi_trips t
  join taxi_zones z
  on (t."DOLocationID" = z."LocationID")
where 
  extract(month from lpep_pickup_datetime) = 10
and "PULocationID" in (
   select "LocationID" 
   from taxi_zones  
   where "Zone"='East Harlem North'
)
group by z."Zone"
order by max_tip desc