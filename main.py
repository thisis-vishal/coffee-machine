MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0,
}
def moneyentry():
    quarter=int(input("Enter the number of quarter you want to enter"))
    dimes=int(input("Enter the number of dimes you want to enter"))
    nickel=int(input("Enter the number of nickel you wnat ot enter"))
    pennies=int(input("enter the number of pennies you want to enter"))
    entered_amount=quarter*0.25 + dimes*0.1 + nickel*0.05 + pennies*0.01
    return entered_amount
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True    
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] = resources[item]-order_ingredients[item]    
def check_amount(type,entered_amount):
    list=MENU[type]
    price=list["cost"]
    if price==entered_amount:
        print(f"“Here is your {type}. Enjoy!”. ")
        resources["money"]= resources["money"]+entered_amount
        make_coffee(type, list["ingredients"])
        machinerun()
    elif price<entered_amount:
        change=entered_amount-price
        print(f"Here is ${change}  dollars in change.")
        print(f"“Here is your {type}. Enjoy!”. ")   
        resources["money"] = resources["money"] + price 
        make_coffee(type, list["ingredients"])
        machinerun()
    else:
        print("“Sorry that's not enough money. Money refunded.”")    
        machinerun()
     
#user choice input

def machinerun():
    water=resources["water"]
    milk=resources["milk"]
    coffee=resources["coffee"]
    money=resources["money"]
    user_choice=input("what would you like ?(espresso/ latte / cappuccino)").lower()
    if user_choice=="report":
        print(f"water : {water}")
        print(f"Milk : {milk}")
        print(f"Cofee : {coffee}")
        print(f"Money: ${money}")
        machinerun()
    elif user_choice=="espresso":
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            entered_amount=moneyentry()
            check_amount("espresso",entered_amount)
    elif user_choice=="latte":
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            entered_amount=moneyentry()
            check_amount("latte",entered_amount)    
    elif user_choice=="cappuccino":
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            entered_amount=moneyentry()
            check_amount("cappuccino",entered_amount)
    elif user_choice=="off":
        False
    else:
        print("invalid choice") 
        machinerun()
machinerun()        
