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

    @staticmethod
    def AddTypeWork(data):
        request = 'insert into WORK_TYPE values (\'' + data + '\')'
        work = sl.connect('work_type.db')
        with work:
            work.execute(request)

    @staticmethod
    def GetTypeWork():
        request = 'select * from WORK_TYPE'
        work = sl.connect('work_type.db')
        result = []
        with work:
            for val in work.execute(request):
                result.append(val)
        return result

    @staticmethod
    def DeleteData(path, name_database):
        database = sl.connect(path)
        cursor = database.cursor()
        request = """delete from """ + name_database
        cursor.execute(request)
        database.commit()


y = Database()
y.AddTypeWork("Чистка")
for val in y.GetTypeWork():
    print(val)
y.DeleteData('work_type.db', "WORK_TYPE")
print('Удаление произошло?')
for val in y.GetTypeWork():
    print(val)

print('Произошло :)')
c = sl.connect('orders.db')
with c:
    database = c.execute('select * from ORDERS')
    for row in database:
        print(row)
