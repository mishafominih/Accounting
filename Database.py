import sqlite3 as sl
from datetime import date


class DataExpenses:
    def __init__(self, expenses_date, price, information):
        self.Date = expenses_date
        self.Price = price
        self.Information = information


class DataOrders:
    def __init__(self, Id=None, number=None, price=None, orders_time= None, type_orders=None,
                 name_customer=None, car=None, orders_date=None, amrt=None):
        self.ID = Id
        self.Number = number
        self.Price = price
        self.Time = orders_time
        self.Type = type_orders
        self.Name = name_customer
        self.Car = car
        self.Date = None
        if orders_date is not None:
            self.Date = str(orders_date)
        self.AMRT = amrt

    @staticmethod
    def __dir__():
        return [['ID', 'Number', 'Name', 'Car', 'Price', 'Time', 'AMRT', 'Date'], ['Type']]


class Database:
    @staticmethod
    def GetExpenses(start_date, end_date):
        request = "select Date, Price, Information from EXPENSES where Date between "
        return Database._GetDataForPeriod('Expenses.db', request, start_date, end_date)

    @staticmethod
    def GetDataForPeriod(start_date, end_date):
        request = "select ID from ORDERS where Date between "
        result = []
        for id_orders in Database._GetDataForPeriod('orders.db', request, start_date, end_date):
            result += Database.Find(DataOrders(Id=id_orders))
        return result

    @staticmethod
    def AddData(data: DataOrders):
        Database._AddOrders(data)

    @staticmethod
    def Find(data_orders: DataOrders):
        if not Database._BadFields(data_orders):
            result_for_orders = Database._GetOrders(data_orders)
        else:
            result_for_orders = None
        result_for_type = []
        id_orders = Database._GetType(data_orders)
        for val in id_orders:
            result_for_type += Database._GetOrders(DataOrders(val))
        if result_for_orders is None:
            return result_for_type
        elif len(id_orders) == 0:
            return result_for_orders
        else:
            return [x for x in result_for_orders if x in result_for_type]

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
    def DeleteExpenses(date, price, info):
        database = sl.connect("Expenses.db")
        cursor = database.cursor()
        request = 'delete from EXPENSES where Date = (\'' + date + '\')' \
                ' and Price = (\'' + price + '\') and Information = (\'' + info + '\')'
        cursor.execute(request)
        database.commit()

    @staticmethod
    def _GetDataForPeriod(path, request, start_date, end_date):
        database = sl.connect(path)
        request += "'" + str(start_date) + "' and '" + str(end_date) + "'"
        result = []
        with database:
            for i in database.execute(request):
                result += i
            return result

    @staticmethod
    def _GetType(data):
        service_type = sl.connect('service_type.db')
        result = []
        if data.Type is None:
            return []
        for val in data.Type:
            request = 'select ID_ORDERS from SERVICE_TYPE where Name = ' + "'" + val + "'"
            with service_type:
                for element in service_type.execute(request):
                    result += element
        return set(result)

    @staticmethod
    def _BadFields(data_orders):
        for val in DataOrders.__dir__()[0]:
            if getattr(data_orders, val) is not None:
                return False
        return True

    @staticmethod
    def _GetOrders(data_orders):
        orders = sl.connect('orders.db')
        service_type = sl.connect('service_type.db')
        request_orders = Database._GetRequestForFind('ORDERS', DataOrders.__dir__()[0], data_orders)
        result = []
        data = []
        with orders, service_type:
            database_orders = (orders.execute(request_orders))
            for val in database_orders:
                data += val
                id_orders = val[0]
                types = []
                for m_type in service_type.execute('select Name from SERVICE_TYPE where ID_ORDERS = '
                                                   + str(id_orders)):
                     types += m_type
                data.append(types)
                result.append(data)
        return result

    @staticmethod
    def _GetRequestForFind(name_database, fields, data):
        request = "select * from " + name_database + " where "
        back_field = False
        for index, val in enumerate(fields):
            field = getattr(data, val)
            if field is not None:
                if len(fields) >= index and back_field:
                    request += " and "
                back_field = True
                request += val + " = "
                if type(field) is str:
                    request += "'" + str(field) + "'" + " "
                else:
                    request += str(field) + " "
        return request

    @staticmethod
    def _AddElement(path, request, data):
        database = sl.connect(path)
        with database:
            database.executemany(request, data)

    @staticmethod
    def _AddOrders(my_order: DataOrders):
        request = 'insert into ORDERS (Number, Name, Car, Price, Time, Date, AMRT) values (?, ?, ?, ?, ?, ?, ?)'
        data = [(my_order.Number, my_order.Name, my_order.Car, my_order.Price, my_order.Time, my_order.Date, my_order.AMRT)]
        Database._AddElement('orders.db', request, data)
        orders = sl.connect('orders.db')
        request = Database._GetRequestForFind('ORDERS', DataOrders.__dir__()[0], my_order)

        with orders:
            for val in orders.execute(request):
                id_orders = val[0]

        request = 'insert into SERVICE_TYPE (ID_ORDERS, Name) values(?, ?)'
        for val in my_order.Type:
            data = [(id_orders, val)]
            Database._AddElement('service_type.db', request, data)


my_type = ['чистка', 'мытье']
y = sl.connect('orders.db')

print(Database.Find(DataOrders(Id=7)))
