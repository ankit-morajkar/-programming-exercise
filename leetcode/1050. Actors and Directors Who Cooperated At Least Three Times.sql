# Write your MySQL query statement below
select actor_id, director_id from(
select director_id, actor_id, count(*) as cnt
from ActorDirector
group by director_id, actor_id
having cnt >=3) e