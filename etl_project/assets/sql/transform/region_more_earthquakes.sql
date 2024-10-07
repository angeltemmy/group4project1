WITH earthquakes as(
	select t1.region as region, count(t1.id) as quantity from table_earthquake_1_data t1
	join table_earthquake_2_data t2 on t1.id = t2.id
	group by t1.region

) select e.region, max(e.quantity) from earthquakes e
  group by e.region, e.quantity
  order by e.quantity DESC
  limit 1