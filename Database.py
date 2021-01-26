import sqlite3 as sl
from datetime import date


class DataExpenses:
    def __init__(self, expenses_date, price, information):
        self.Date = expenses_date
        self.Price = price
        self.Information = information


class DataOrders:
    def __init__(self, number, price, orders_time, type_orders, name_customer, car, orders_date, amrt):
        self.Number = number
        self.Price = price
        self.Time = orders_time
        self.Type = type_orders
        self.Name = name_customer
        self.Car = car
        self.date = orders_date
        self.AMRT = amrt


class Database:
    @staticmethod
    def GetExpenses(start_date, end_date):
        expenses = sl.connect('Expenses.db')
        request = "select Price from EXPENSES where Date between '" + str(start_date) + "' and '" +\
                  str(end_date) + "'"
        result = []
        with expenses:
            for i in expenses.execute(request):
                result.append(i)
            return result

    @staticmethod
    def AddData(data: DataOrders):
        Database._AddCustomer(data)
        Database._AddOrders(data)

    @staticmethod
    def Find(number):
        customers = sl.connect('customer.db')
        orders = sl.connect('orders.db')
        result = []
        with orders, customers:
            result += orders.execute(
                'select * from ORDERS where Number = ' + str(number)
            )
            result += (customers.execute(
                'select Name, Car from CUSTOMERS where Number = ' + str(number)
            ))
        return result

    @staticmethod
    def AddExpenses(my_expenses):
        request = 'insert into EXPENSES (Date, Price, Information) values (?, ?, ?)'
        data = [(my_expenses.Date, my_expenses.Price, my_expenses.Information)]
        Database._AddElement('Expenses.db', request, data)

    @staticmethod
    def AddTypeWork(data):
        request = 'insert into WORK_TYPE values (\'' + data + '\')'
        work = sl.connect('work_type.db')
        with work:
            work.execute(request)

    @staticmethod
    def GetTypesWork():
        request = 'select * from WORK_TYPE'
        work = sl.connect('work_type.db')
        result = []
        with work:
            for val in work.execute(request):
                result.append(val[0])
        return result

    @staticmethod
    def DeleteData(path, name_database):
        database = sl.connect(path)
        cursor = database.cursor()
        request = """delete from """ + name_database
        cursor.execute(request)
        database.commit()

    @staticmethod
    def DeleteWork(work):
        database = sl.connect("work_type.db")
        cursor = database.cursor()
        request = 'delete from WORK_TYPE where name = (\'' + work + '\')'
        cursor.execute(request)
        database.commit()

    @staticmethod
    def _AddElement(path, request, data):
        database = sl.connect(path)
        with database:
            database.executemany(request, data)

    @staticmethod
    def _AddCustomer(my_customer):
        if len(Database.Find(my_customer.Number)) == 0:
            request = 'insert into CUSTOMERS (Number, Name, Car) values (?, ?, ?)'
            data = [(my_customer.Number, my_customer.Name, my_customer.Car)]
            Database._AddElement('customer.db', request, data)

    @staticmethod
    def _AddOrders(my_order):
        request = 'insert into ORDERS (Number, Price, Time, Date, AMRT) values (?, ?, ?, ?, ?)'
        data = [(my_order.Number, my_order.Price, my_order.Time, my_order.date, my_order.AMRT)]
        Database._AddElement('orders.db', request, data)
        id_orders = Database.Find(my_order.Number)[0][0]
        request = 'insert into SERVICE_TYPE (ID_ORDERS, Number, Name) values(?, ?, ?)'
        for val in my_order.Type:
            data = [(id_orders, my_order.Number, val)]
            Database._AddElement('service_type.db', request, data)


z = sl.connect('service_type.db')
t = ['чистка', 'мойка', 'что-то еще']
Database.DeleteData('Expenses.db', 'EXPENSES')
y = DataExpenses(date.today(), 300, 'Чистка')
x = DataOrders(102, 10, 2, t, 'Дима', 'Honda', date.today(), 300)
start = date(2010, 10, 10)
end = date(2022, 1, 30)
print(Database.GetExpenses(start, end))
