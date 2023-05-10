select name, sum(amount) as balance
from users join transactions using (account)
group by name
having sum(amount)>10000;