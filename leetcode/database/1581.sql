with not_vis as(
    select customer_id
    from visits a
    where a.visit_id not in (select b.visit_id from transactions b)
)
select customer_id, count(*) as count_no_trans
from not_vis
group by 1;