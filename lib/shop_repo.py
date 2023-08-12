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


    def find_by_item(self, item):
        rows = self._connection.execute("SELECT items.id AS item_id, items.name, items.price, items.quantity, " \
                                        "orders.id AS order_id, orders.customer_name, orders.order_date " \
                                        "FROM items JOIN items_orders ON items_orders.item_id = items.id " \
                                        "JOIN orders ON items_orders.order_id = orders.id " \
                                        "WHERE items.name = %s" , [item])
        orders = []
        for row in rows:
            order = Order(row['order_id'], row['customer_name'], row['order_date'])
            orders.append(order)
    
        return Item(rows[0]['item_id'], rows[0]['name'], rows[0]['price'], rows[0]['quantity'], orders)


    def find_by_order(self, order_id):
        rows = self._connection.execute("SELECT items.id AS item_id, items.name, items.price, items.quantity, " \
                                        "orders.id AS order_id, orders.customer_name, orders.order_date " \
                                        "FROM items JOIN items_orders ON items_orders.item_id = items.id " \
                                        "JOIN orders ON items_orders.order_id = orders.id " \
                                        "WHERE orders.id = %s" , [order_id])
        items = []
        for row in rows:
            item = Item(row['item_id'], row['name'], row['price'], row['quantity'])
            items.append(item)

        return Order(rows[0]['order_id'], rows[0]['customer_name'], rows[0]['order_date'], items)


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