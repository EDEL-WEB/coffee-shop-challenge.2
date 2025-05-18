from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Anna")
c2 = Customer("Ben")
cf = Coffee("Latte")

c1.create_order(cf, 5.0)
c2.create_order(cf, 6.0)
c2.create_order(cf, 3.0)

print(cf.num_orders())            # 3
print(cf.average_price())         # 4.67
print(Customer.most_aficionado(cf).name)  # Ben
