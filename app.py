from lib.database_connection import DatabaseConnection
from lib.shop_repo import ShopRepository
from lib.item import Item
from lib.order import Order

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/shop_manager_database.sql")
        self.shop_repo = ShopRepository(self._connection)

    def run(self):
        on = True
        while on: 
            choice = input("What would you like to do? \n1 - List all items \n2 - Create new item " \
                            "\n3 - List all orders \n4 - Create new order \n5 - Turn off \n")
            
            if int(choice) == 1:
                self.get_table('items')

            elif int(choice) == 2:
                self.create_record('items')

            elif int(choice) == 3:
                self.get_table('orders')
            
            elif int(choice) == 4:
                self.create_record('orders')

            else:
                on = False


    def get_table(self, table_name):
        table_info = self.shop_repo.all(table_name)
        for info in table_info:
            print(info)
    
    def create_record(self, table_name):
        if table_name == 'items':
            name = input('What is the name of item: ')
            price = input('Price: ')
            quantity = input('Quantity: ')
            self.shop_repo.create_item(Item(None, name, float(price), int(quantity)))
            print('Item created')
            self.get_table('items')

        elif table_name == 'orders':
            name = input('What is the name of the customer: ')
            date = input('Date: ')
            self.shop_repo.create_item(Order(None, name, date))
            print('order created')


if __name__ == '__main__':
    app = Application()
    app.run()