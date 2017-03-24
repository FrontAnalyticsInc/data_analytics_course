
-- Show tables
show databases;
use frontanalytics;
show tables;

-- Look at first table
select * from frontanalytics.ipaddress_to_gaclientid limit 10;
select count(*) from ipaddress_to_gaclientid;
select distinct url from ipaddress_to_gaclientid;


--
select url, form_inputs, count(*) 
from ipaddress_to_gaclientid
group by url, form_inputs
order by url, count(*) desc;

-- This is a comment
select * from ipaddress_to_gaclientid
where form_input_value = 'alton';


-- next table
show tables;
select * from trackingcodes;

select * from webinar;


-- what is the hitrate for the survey (observation) by hour between two dates
select 
			date(created_at) as dt, 
			hour(created_at) as hr, 
            ipaddress, 
			count(*) as n_observations
		from ipaddress_to_gaclientid
		where date(created_at) > '2017-03-06'
		and url = 'lunch-and-learn-survey'
		group by date(created_at), hour(created_at), ipaddress 
        order by date(created_at), hour(created_at);



select dt, hr, count(*) as n_ipaddress, avg(n_observations) as avg_n_obs_per_ip from 
		( select 
			date(created_at) as dt, 
			hour(created_at) as hr, 
            ipaddress, 
			count(*) as n_observations
		from ipaddress_to_gaclientid
		where date(created_at) > '2017-03-06'
		and url = 'lunch-and-learn-survey'
		group by date(created_at), hour(created_at), ipaddress 
        order by date(created_at), hour(created_at) ) 
tmp_tbl
group by dt, hr
order by dt, hr;



-- what about unique users?
select * from ipaddress_to_gaclientid
where date(created_at) = '2017-03-06'
and url = 'lunch-and-learn-survey';













