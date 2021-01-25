import sqlite3 as sl


class DataOrders:
    def __init__(self, number, price, time, type_orders, name_customer, car):
        self.Number = number
        self.Price = price
        self.Time = time
        self.Type = type_orders
        self.Name = name_customer
        self.Car = car


class Database:

    @staticmethod
    def _AddElement(path, request, data):
        database = sl.connect(path)
        with database:
            database.executemany(request, data)

    @staticmethod
    def AddCustomer(my_customer):
        request = 'insert into CUSTOMERS (Number, Name, Car) values (?, ?, ?)'
        data = [(my_customer.Number, my_customer.Name, my_customer.Car)]
        Database._AddElement('customer.db', request, data)

    @staticmethod
    def Find(number):
        customers = sl.connect('customer.db')
        orders = sl.connect('orders.db')
        result = []
        request = 'select * from ORDERS where Number = ' + str(number)
        with orders:
            result += orders.execute(request)
        request = 'select * from CUSTOMERS where Number = ' + str(number)
        with customers:
            result += customers.execute(request)
        return result

    @staticmethod
    def AddOrders(my_order):
        request = 'insert into ORDERS (Number, Price, Time, Type) values (?, ?, ?, ?)'
        data = [(my_order.Number, my_order.Price, my_order.Time, my_order.Type)]
        Database._AddElement('orders.db', request, data)


x = Database()
print(x.Find(1))
