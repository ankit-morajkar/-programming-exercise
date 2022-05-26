# Write your MySQL query statement below

select name as Employee
from Employee as e1
inner join (select id as m_id, salary as m_salary from Employee) as e2
on e1.managerId = e2.m_id and e1.salary > e2.m_salary