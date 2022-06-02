# Write your MySQL query statement below

select department, name as employee, salary from (
select a.*, b.name as department, 
dense_rank() over (partition by departmentId order by salary desc) as dr
from employee a
left join department b
on a.departmentId = b.id
) c 
where dr = 1