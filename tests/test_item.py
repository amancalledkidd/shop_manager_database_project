from lib.item import Item 

"""
test for field intialise
"""

def test_class_init():
    item = Item(1, 'Orange', 0.30, 10)
    assert item.id == 1
    assert item.name == 'Orange'
    assert item.price == 0.30
    assert item.quantity == 10

"""
test equality works
"""

def test_equality_in_class():
    item1 = Item(1, 'Orange', 0.30, 10)
    item2 = Item(1, 'Orange', 0.30, 10)
    assert item1 == item2

"""
create instance of class
returns formated string
"""

def test_class_formatting():
    item1 = Item(1, 'Orange', 0.30, 10)
    assert str(item1) == 'Item(1, Orange, 0.30, 10)'