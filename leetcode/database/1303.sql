with team_size as (
    select team_id, count(employee_id) as size
    from employee
    group by team_id
)
select a.employee_id, b.size as 'team_size'
from employee a join team_size b on a.team_id=b.team_id;