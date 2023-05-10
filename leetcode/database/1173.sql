with order_im as(
    select count(delivery_id) orders
    from delivery
    where order_date=customer_pref_delivery_date
), order_sch as(
    select count(delivery_id) orders
    from delivery
    where order_date!=customer_pref_delivery_date
)
select round((a.orders/(a.orders+b.orders))*100,2) as immediate_percentage
from order_im a, order_sch b;