# Write your MySQL query statement below
select id from
    (
    select *, lag(recordDate) over(order by recordDate) prev_date,
        lag(temperature) over(order by recordDate) prev_temp
    from Weather
        ) e 
        where temperature>prev_temp 
        and DATEDIFF(prev_date, recordDate)=-1