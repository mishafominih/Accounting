import sqlite3 as sl


class DataOrders:
    def __init__(self, id, number, price, time, type_orders, name_customer, car):
        self.Id = id
        self.Number = number
        self.Price = price
        self.Time = time
        self.Type = type_orders
        self.Name = name_customer
        self.Car = car


class Database:
    customer = sl.connect('customer.db')

    def AddOrders(self, my_order):
        orders = sl.connect('orders.db')
        request = 'insert into ORDERS (ID, Number, Price, Time, Type) values (?, ?, ?, ?, ?)'
        data = [(my_order.Id, my_order.Number, my_order.Price, my_order.Time, my_order.Type)]
        with orders:
            orders.executemany(request, data)


c = sl.connect('orders.db')
with c:
    database = c.execute('select * from ORDERS')
    for row in database:
        print(row)
