select sum(miles_lt1),
	sum(miles_1to3),
	sum(miles_3to7),
	sum(miles_7to10),
	sum(miles_gt10)
from (
SELECT
	case
	when trip_distance < 1
	then 1 else 0
	end miles_lt1,
	case
	when trip_distance > 1 and trip_distance <= 3
	then 1 else 0
	end miles_1to3,
	case when trip_distance > 3 and trip_distance<= 7
	then 1 else 0
	end miles_3to7,
	case when trip_distance > 7 and trip_distance<= 10
	then 1 else 0
	end miles_7to10,
	case when trip_distance > 10
	then 1 else 0
	end miles_gt10

FROM public.green_taxi_trips t
where extract(month from lpep_pickup_datetime) = 10
) t
