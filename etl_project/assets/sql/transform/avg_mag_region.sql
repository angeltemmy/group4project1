--What is the average magnitude of earthquakes in each country/region? 
select t1.region, avg(t2.mag) from table_earthquake_1_data t1
join table_earthquake_2_data t2 on t1.id = t2.id
group by t1.region