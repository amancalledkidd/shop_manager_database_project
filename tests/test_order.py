from lib.order import Order 

"""
test for field intialise
"""

def test_class_init():
    order = Order(1, 'Oran', '23/02/2023')
    assert order.id == 1
    assert order.customer_name == 'Oran'
    assert order.order_date == '23/02/2023'

"""
test equality works
"""

def test_equality_in_class():
    order1 = Order(1, 'Oran', '23/02/2023')
    order2 = Order(1, 'Oran', '23/02/2023')
    assert order1 == order2

"""
create instance of class
returns formated string
"""

def test_class_formatting():
    order1 = Order(1, 'Oran', '23/02/2023')
    assert str(order1) == 'Order(1, Oran, 23/02/2023)'