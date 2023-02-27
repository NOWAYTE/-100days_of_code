from game_data import resources, MENU
from logo import logo

print(logo)
print("welcome to the coffee making machine")
profit = 0


def coffee(name, ingredients):
    for ist in ingredients:
        resources[ist] -= ingredients[ist]

    print(f"here is your {name}")


def resource(init_resources):
    for ing in init_resources:
        if init_resources[ing] >= resources[ing]:
            print(f"daang you are out of lack not enough{ing}")
            return False
    return True


def coins():
    print("insert coins")
    total = int(input("how many quarters ?")) * 0.25
    total += int(input("how many dimes ?")) * 0.1
    total += int(input("how many nickles ?")) * 0.05
    total += int(input("how many pennies ?")) * 0.01

    return total


def transaction(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        print(f"here are your {change}")
        global profit
        profit += cost
        return True
    else:
        print("get some money friend")
        return False


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"ml")
        print(f"Milk: {resources['milk']}")
        print(f"ml")
        print(f"Coffee: {resources['coffee']}")
        print(f"g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        if resource(drink['ingredients']):
            payment = coins()
            if transaction(payment, drink['cost']):
                coffee(choice, drink['ingredients'])
