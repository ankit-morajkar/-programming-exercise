# Write your MySQL query statement below
select day, round(canned2/total,2) as 'cancellation rate' 
from(
    select *, canned2+completed2 total
    from(
        select day, 
        case when canned is Null then 0 else canned end as canned2, 
        case when completed is Null then 0 else completed end as completed2
        from(
            select distinct (k.request_at) day, canned, completed
            from (select * from trips) k
            inner join
                (select users_id as c_id 
                from users where role = 'client' and banned = 'No') unbanned_clients1
            on client_id = c_id
            inner join
                (select users_id as d_id 
                from users where role = 'driver' and banned = 'No') unbanned_drivers1
            on driver_id = d_id
            left join
            (
                select request_at, count(*) canned 
                from (
                    select *
                    from trips
                    inner join
                        (select users_id as c_id 
                         from users where role = 'client' and banned = 'No') unbanned_clients
                     on client_id = c_id
                    inner join
                        (select users_id as d_id 
                         from users where role = 'driver' and banned = 'No') unbanned_drivers
                     on driver_id = d_id
                    where status like '%cancelled%') x
                group by request_at) a
            on k.request_at = a.request_at
            left join(
                select request_at, count(*) completed 
                from (
                    select *
                    from trips
                    inner join
                        (select users_id as c_id 
                         from users where role = 'client' and banned = 'No') unbanned_clients
                     on client_id = c_id
                    inner join
                        (select users_id as d_id 
                         from users where role = 'driver' and banned = 'No') unbanned_drivers
                     on driver_id = d_id
                    where status like '%completed%') y
                group by request_at) b
            on k.request_at = b.request_at) p
        ) l
    ) m
where day >='2013-10-01' and day <= '2013-10-03'