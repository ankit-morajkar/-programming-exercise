# Write your MySQL query statement below

select distinct num consecutivenums from
(select *, lag(next_num) over (order by id) next_next_num from
(select *, lag(num) over (order by id) next_num
from logs) e) f
where num = next_num and next_num = next_next_num