# Shop manager Model and Repository Classes Design Recipe

## 1. Design and create the Table

[Table Schema](./shop_manager_table_schema.md)


## 2. Test SQL seeds

```sql
DROP TABLE IF EXISTS items CASCADE;


CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name text,
    price numeric,
    quantity int
);

DROP TABLE IF EXISTS orders;


CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name text,
    order_date date
);

DROP TABLE IF EXISTS items_orders;


CREATE TABLE items_orders (
    item_id int,
    order_id int,
    constraint fk_item foreign key(item_id) references items(id) on delete cascade,
    constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
    PRIMARY KEY (item_id, order_id)
);

INSERT INTO items ("name", "price") VALUES
("Apple", 0.50, 10),
("Bread", 0.75, 6),
("Tofu", 2.50 , 4),
("Spinach", 1.50, 20),
("Chocolate", 3.50, 55),
("Rice", 1.00, 43),
("Avocado", 2.00, 11),
("Lentils", 0.90, 34),
("Ice cream", 3.75, 23);


INSERT INTO orders ("customer_name", "order_date") VALUES
("Kumani", 08/09/23),
("K", 27/12/23),
("man", 01/02/24),
("Dave", 02/05/23),
("Moes", 05/05/23),
("Mala", 15/11/23),
("Kumani", 02/01/24);

INSERT INTO items_orders ("customer_name", "order_date") VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(5, 3),
(6, 2),
(7, 1),
(6, 3),
(2, 4),
(3, 4);

```

## 3. class names


```python
# Table name: items

# Model class
# (in lib/item.py)
class item

# Table name: orders

# Model class
# (in lib/order.py)
class order


# Repository class
# (in lib/shop_repo.py)
class ShopRepository

```

## 4. Model class implementaion


```python
# EXAMPLE
# Table name: items

# Model class
# (in lib/items.py)

class Item:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.price = 0.00
        self.quantity = 0



# Table name: orders

# Model class
# (in lib/order.py)
class Order:
    def __init__(self):
        self.id = 0
        self.customer_name = ""
        self.order_date = 1/1/1999



```

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# Table name: items
# Table name: orders
# Table name: items_orders

# Repository class
# (in lib/shop_repo.py)

class ShopRepository():

    # Selecting all records
    # No arguments
    def all():
        # Creates SQL query
        # finds all records in both tables
        # Returns all records
        pass

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

    def creates(self):
        # adds new record to one of the tables
        # Returns none
        pass

    def update(self):
        # updates record to one of the tables
        # Returns none

    def delete(self):
        # deletes record of one of the tables
        # returns none
    

```

## 6. Write Test Examples

```python
# EXAMPLES

"""
creeate instance 
call all
returns all database tables
"""

def test_all_works(db_connection):
    db_connection.seed('seeds/shop_manger_database.sql')
    shop_repo = ShopRepository(db_connection):

    call all
    return list of all records




```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->