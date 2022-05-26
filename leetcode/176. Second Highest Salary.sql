# Write your MySQL query statement below
select
  (
select distinct salary as SecondHighestSalary1 from
(select *, dense_Rank() over(order by salary desc) as dr from Employee) e
where dr = 2
      ) as SecondHighestSalary