# Write your MySQL query statement below

select Department, name as Employee, salary from(
select e.*, dense_rank() over (partition by departmentId order by salary desc) as dr, d.name as Department
from employee e
left join department d
on departmentId = d.id) f where dr <4