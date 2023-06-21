'''
    I did not write any classes myself. 
    This was just a practise to use pre-made classes
'''

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
menu = Menu()

while True:
    options = menu.get_items()
    order = input(f"What would you like? {options}: ")
    if order == "off":
        break
    elif order == "report":
        cm.report()
        mm.report()
    else:
        ordered_drink = menu.find_drink(order)
        if cm.is_resource_sufficient(ordered_drink):
            if mm.make_payment(ordered_drink.cost):
                cm.make_coffee(ordered_drink)