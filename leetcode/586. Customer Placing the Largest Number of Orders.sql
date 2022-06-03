# Write your MySQL query statement below
select customer_number from(
select *, row_number() over (order by cnt desc) as rn from(
select customer_number, count(*) as cnt 
from orders
group by customer_number) e) f where rn = 1