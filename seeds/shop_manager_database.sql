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