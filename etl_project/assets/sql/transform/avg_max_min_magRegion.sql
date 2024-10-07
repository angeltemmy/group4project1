select t1.region, t2.mag,
COUNT(t1.id) OVER(PARTITION BY t1.id) AS CountOfEarthquakes,
AVG(t2.mag) OVER(PARTITION BY t1.id) AS AVGOfEarthquakes,
MAX(t2.mag) OVER(PARTITION BY t1.id) AS MAXofEarthquakes,
MIN(t2.mag) OVER(PARTITION BY t1.id) AS MINofEarthquakes
from table_earthquake_1_data t1
join table_earthquake_2_data t2 on t1.id = t2.id