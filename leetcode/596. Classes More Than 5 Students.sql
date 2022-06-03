# Write your MySQL query statement below

select class from(
select class, count(*) as stus
from courses
group by class
having stus >=5) e