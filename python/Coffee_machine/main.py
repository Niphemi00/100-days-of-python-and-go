MENU = {
    "Expresso" : {
        "Ingredients" : {
            "Water": 50,
            "Coffee" : 18,
            "Milk": 0
        },
        "Cost" : 1.50
    },
    "Latte" : {
        "Ingredients" : {
            "Water": 200,
            "Milk": 150,
            "Coffee" : 24
        },
        "Cost" : 2.50
    },
    "Cappuccino" : {
        "Ingredients" : {
            "Water": 250,
            "Milk": 100,
            "Coffee" : 24
        },
        "Cost" : 3.00
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}
def report(details):
    return f"\n  Water: {details['Water']}ml\n  Milk: {details['Milk']}ml\n  Coffee: {details['Coffee']}g\n  Money: ${details['Money']}"


def making_drink(coffee_drink_name):
    resources['Water']-= MENU[coffee_drink_name]['Ingredients']['Water']
    resources['Milk']-= MENU[coffee_drink_name]['Ingredients']['Milk']
    resources['Coffee']-= MENU[coffee_drink_name]['Ingredients']['Coffee']
    return resources

def payment():
    print("\nPayment determines if your drink would be processed (COINS ALONE).")
    quaters = int(input("How many quaters are you paying: ")) * 0.25
    dimes = int(input("How many dimes are you paying: ")) * 0.1
    nickel = int(input("How many nickels are you paying: ")) * 0.05
    pennies = int(input("How many pennies are you paying: ")) * 0.01
    total = quaters + dimes + nickel + pennies
    return total

def refill_ingredients():
        print(f"\nResources are insufficient to make the {prompt}")
        print("\nAsk the barrister to refill the coffee machine ingredients compartment before the machine makes the order")
        refill = input("Wanna refill: ").lower()
        if refill == 'yes':
            resources = {
                "Water": 300,
                "Milk": 200,
                "Coffee": 100,
                "Money": 0
            }

def resource_checker(resource):
    print(f"{prompt} costs ${MENU[prompt]["Cost"]}")
    if resources['Water'] >= 100 and resources['Milk'] >= 50 and resources['Coffee'] >= 18:
        total_money = payment()
        if total_money >= MENU[prompt]["Cost"]:
            change = total_money - MENU[prompt]["Cost"]
            resources['Money'] = total_money - change
            print(f"\nYour {prompt} is served, here's your change ${change}")
            print(making_drink(prompt))
        else:
            print("\nInsufficient payment...Money refunded!!!")
    elif resources['Water'] < 100 or resources['Milk'] < 50 or resources['Coffee'] <= 18:
        refill_ingredients()
        report(resources)
power = True
while power:
    prompt = input("What would you like? (expresso/latte/cappauccino): ").capitalize()
    if prompt == 'Expresso' :
        resource_checker(resources)
    elif prompt == 'Latte':
        resource_checker(resources)
    elif prompt == 'Cappauccino':
        resource_checker(resources)
    elif prompt == 'Report':
        print(report(resources))
    elif prompt == 'Off':
        print("\nGoing off....")
        print("\nGoodBye!!")
        quit()
    else:
        print("\nWrong Input!!!\n")

