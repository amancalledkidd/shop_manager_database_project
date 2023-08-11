DROP TABLE IF EXISTS items CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS items_orders;

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name text,
    price numeric,
    quantity int
);




CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name text,
    order_date text
);




CREATE TABLE items_orders (
    item_id int,
    order_id int,
    constraint fk_item foreign key(item_id) references items(id),
    constraint fk_order foreign key(order_id) references orders(id),
    PRIMARY KEY (item_id, order_id)
);

INSERT INTO items ("name", "price", "quantity") VALUES ('Apple', 0.50, 10);
INSERT INTO items ("name", "price", "quantity") VALUES ('Bread', 0.75, 6);
INSERT INTO items ("name", "price", "quantity") VALUES ('Tofu', 2.50 , 4);
INSERT INTO items ("name", "price", "quantity") VALUES ('Spinach', 1.50, 20);
INSERT INTO items ("name", "price", "quantity") VALUES ('Chocolate', 3.50, 55);
INSERT INTO items ("name", "price", "quantity") VALUES ('Rice', 1.00, 43);
INSERT INTO items ("name", "price", "quantity") VALUES ('Avocado', 2.00, 11);
INSERT INTO items ("name", "price", "quantity") VALUES ('Lentils', 0.90, 34);
INSERT INTO items ("name", "price", "quantity") VALUES ('Ice cream', 3.75, 23);


INSERT INTO orders ("customer_name", "order_date") VALUES ('Kumani', '08/09/23');
INSERT INTO orders ("customer_name", "order_date") VALUES ('K', '12/27/22');
INSERT INTO orders ("customer_name", "order_date") VALUES ('man', '01/02/22');
INSERT INTO orders ("customer_name", "order_date") VALUES ('Dave', '02/05/23');
INSERT INTO orders ("customer_name", "order_date") VALUES ('Moes', '05/05/23');
INSERT INTO orders ("customer_name", "order_date") VALUES ('Mala', '9/11/23');
INSERT INTO orders ("customer_name", "order_date") VALUES ('Kumani', '02/01/24');

INSERT INTO items_orders ("item_id", "order_id") VALUES (1, 1);
INSERT INTO items_orders ("item_id", "order_id") VALUES (2, 1);
INSERT INTO items_orders ("item_id", "order_id") VALUES (3, 1);
INSERT INTO items_orders ("item_id", "order_id") VALUES (4, 2);
INSERT INTO items_orders ("item_id", "order_id") VALUES (5, 3);
INSERT INTO items_orders ("item_id", "order_id") VALUES (6, 2);
INSERT INTO items_orders ("item_id", "order_id") VALUES (7, 1);
INSERT INTO items_orders ("item_id", "order_id") VALUES (6, 3);
INSERT INTO items_orders ("item_id", "order_id") VALUES (2, 4);
INSERT INTO items_orders ("item_id", "order_id") VALUES (3, 4);