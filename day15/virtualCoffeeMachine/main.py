from stats import MENU, resources

menu = MENU
res = resources

#TODO Just the start. I know what to do, just pushing this for now
def getReport(*args):
    '''Prints the remaining resources'''
    return res

machine_functions = {"report" : getReport}
while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        break
    
    new_function = machine_functions[order]
    print(new_function({}))    