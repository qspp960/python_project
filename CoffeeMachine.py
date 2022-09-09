MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}


profit = 0
is_on = True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Here is your coffee!!")


def is_transaction_successful(received_money, drink_cost):
    if received_money >= drink_cost:
        change = round(received_money-drink_cost,2)
        print(f"change money is ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry")
        return False


def process_coins():
    print("insert your coins!!")
    total = int(input("quarters:")) * 0.25
    total += int(input("dimes:")) * 0.1
    total += int(input("nickle:")) * 0.05
    total += int(input("pennies:")) * 0.01
    return total


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Its not enough {item}")
            return False
    return True


while is_on:
    choice = input("What would you like coffee? (espresso,latte,caffuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water {resources['water']}:")
        print(f"milk:{resources['milk']}")
        print(f"coffee:{resources['coffee']}")
        print(f"money:${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


