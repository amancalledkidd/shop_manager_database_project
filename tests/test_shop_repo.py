from lib.item import Item
from lib.order import Order
from lib.shop_repo import ShopRepository

"""
creeate instance 
call all on table of choice as string
returns all database tables
"""
def test_all_orders_works(db_connection):
    db_connection.seed('seeds/shop_manager_database.sql')
    shop_repo = ShopRepository(db_connection)

    orders = shop_repo.all('orders')
    assert orders == [
        Order(1, 'Kumani', '08/09/23'),
        Order(2, 'K', '12/27/22'),
        Order(3, 'man', '01/02/22'),
        Order(4, 'Dave', '02/05/23'),
        Order(5, 'Moes', '05/05/23'),
        Order(6, 'Mala', '9/11/23'),
        Order(7, 'Kumani', '02/01/24')
    ]
    



def test_all_items_works(db_connection):
    db_connection.seed('seeds/shop_manager_database.sql')
    shop_repo = ShopRepository(db_connection)

    items = shop_repo.all('items')
    assert items == [
        Item(1, "Apple", 0.50, 10),
        Item(2, "Bread", 0.75, 6),
        Item(3, "Tofu", 2.50 , 4),
        Item(4, "Spinach", 1.50, 20),
        Item(5, "Chocolate", 3.50, 55),
        Item(6, "Rice", 1.00, 43),
        Item(7, "Avocado", 2.00, 11),
        Item(8, "Lentils", 0.90, 34),
        Item(9, "Ice cream", 3.75, 23),
    ]
    

# "SELECT * FROM items " \
# "JOIN items_orders ON items_orders.item_id = items.id " \
# "JOIN orders ON items_orders.order_id = orders.id")