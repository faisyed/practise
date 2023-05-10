select a.id as id,a.year as year, case when b.npv is null then 0 else b.npv end as npv
from queries a left join npv b on a.id=b.id and a.year=b.year
order by 1;