from lib.item import Item
from lib.order import Order


class ShopRepository():

    def __init__(self, connection):
        self._connection = connection


    def all(self, table):
        table_contents = []
        if table == 'items':
            rows = self._connection.execute("SELECT * FROM items")
            
            for row in rows:
                item = Item(row['id'], row['name'], row['price'], row['quantity'])
                table_contents.append(item)
            return table_contents

        elif table == 'orders':
            rows = self._connection.execute("SELECT * FROM orders")
            
            for row in rows:
                order = Order(row['id'], row['customer_name'], row['order_date'])
                table_contents.append(order)
            return table_contents


    def find_by_id(self):
        # Parameters: table: SQL table
        # id: int represent id of table
        # Creates SQL query
        pass

    def find_by_item(self):
        # Creates SQL query
        # finds orders by items tables
        # Returns related orders
        pass


    def find_by_order(self):
        # Creates SQL query
        # finds items by order tables
        # Returns related items
        pass

    def create_item(self, item):
        self._connection.execute('INSERT INTO items (name, price, quantity) VALUES (%s, %s, %s)', 
                                [item.name, item.price, item.quantity])
        return None
    
    def create_order(self, order):
        self._connection.execute('INSERT INTO orders (customer_name, order_date) VALUES (%s, %s)', 
                                [order.title, order.release_year])
        return None
    
    def link_item_to_order(self, item, order):
        self._connection.execute('INSERT INTO items_orders (item_id, order_id) VALUES (%s, %s)', 
                                [item.id, order.id])
        return None

    def update(self):
        # updates record to one of the tables
        # Returns none
        pass

    def delete(self):
        # deletes record of one of the tables
        # returns none
        pass