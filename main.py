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


money = 0
machine_on = True

print("="*50)
print(" ☕ WELCOME TO REDDY'S COFFEE MACHINE PROJECT ☕")
print("="*50)
while machine_on:
    choice = input("What would you like : (espresso/latte/cappuccino) : ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money:.2f}")
    elif choice == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            print("please insert coins.....")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
            if total >= MENU["espresso"]["cost"]:
                espresso_cost = MENU["espresso"]["cost"]
                print("✅ Transaction successful!")
                print("Here is your ☕ espresso.....ENJOY!!!!")
                print(f"Take your change : ${total-espresso_cost:.2f}")
                money+=espresso_cost
                resources["water"]-= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"]-= MENU["espresso"]["ingredients"]["coffee"]
            else:
                print("Sorry not enough money...money refunded")
        else:
            print("Sorry not enough resources")
    elif choice == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and \
        resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and \
        resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:

            print("please insert coins.....")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))

            total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

            if total >= MENU["latte"]["cost"]:
                print("✅ Transaction successful!")
                print("Here is your ☕ latte.....ENJOY!!!!")
                print(f"Take your change : ${total - MENU['latte']['cost']:.2f}")

                money += MENU["latte"]["cost"]
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            else:
                print("Sorry not enough money...money refunded")
        else:
            print("Sorry not enough resources")
    elif choice == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and \
        resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and \
        resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:

            print("please insert coins.....")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))

            total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

            if total >= MENU["cappuccino"]["cost"]:
                print("✅ Transaction successful!")
                print("Here is your ☕ cappuccino.....ENJOY!!!!")
                print(f"Take your change : ${total - MENU['cappuccino']['cost']:.2f}")

                money += MENU["cappuccino"]["cost"]
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            else:
                print("Sorry not enough money... money refunded")
        else:
            print("Sorry not enough resources")
    else:
        print("Invalid choice. Please choose espresso, latte, cappuccino, report, or off.")