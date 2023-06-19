from stats import MENU, resources

current_drink = {}

#TODO give back the amount of money that was over the price of purchase / refund the money if there's not enough
#TODO reduce the amount of incredients from the resources if everything else is fine and then print the result

def getReport():
    '''Prints the remaining resources'''
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")

def checkResources(ordered_drink):
    for i in ordered_drink:
        if ordered_drink[i] > resources[i]:
            print(f"Sorry not enough {i}")
            return False
    return True

def checkMoney(ordered_drink):
    if ordered_drink > resources['money']:
        print("Sorry not enough money inserted")
        return False
    else:
        return True

def reduce_resources(res, drink):
    pass

while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        break
    elif order == "report":
        getReport()
    else:
        current_drink = MENU[order]
        if checkResources(current_drink['ingredients']):
            inserted_money = float(input("Please insert money: $"))
            resources["money"] =+ inserted_money
            if checkMoney(current_drink['cost']):
                taken_resources = reduce_resources(resources, current_drink['ingredients'])
                
