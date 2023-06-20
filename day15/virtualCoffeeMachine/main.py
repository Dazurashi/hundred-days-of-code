'''
    Program tries to mimic a coffee machine.
    User is asked which kind of drink they want.
    User will then insert money into the machine and if it's enough, their drink is made.
    Resources are reduced mased on which kind of drink it was.
    Other functions are "off" and "report"
'''

from stats import MENU, resources


def getReport():
    '''Prints the remaining resources'''
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")

def checkResources(ordered_drink):
    for i in ordered_drink:
        if ordered_drink[i] > resources[i]:
            print(f"Sorry not enough {i}")
            return False
    return True

def checkMoney(money, cost):
    if money < cost:
        print("Sorry not enough money inserted. Money refunded.")
        return False
    else:
        change = money - cost
        print(f"Here's your ${change} change")
        resources['money'] += cost
        return True

def get_payment():
    return float(input("Please insert money: $"))

def make_order(name, ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here's your {name}.")

while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        break
    elif order == "report":
        getReport()
    else:
        current_drink = MENU[order]
        if checkResources(current_drink['ingredients']):
            inserted_money = get_payment()
            if checkMoney(inserted_money, current_drink['cost']):
                make_order(order, current_drink['ingredients'])
            
                
