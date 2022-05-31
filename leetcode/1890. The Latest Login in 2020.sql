# Write your MySQL query statement below
select user_id, time_stamp as last_stamp from (
select *, Row_number() over(partition by user_id order by time_stamp desc) rn
from (
    select * from Logins
    where year(time_stamp) = 2020
    ) e ) f where rn = 1