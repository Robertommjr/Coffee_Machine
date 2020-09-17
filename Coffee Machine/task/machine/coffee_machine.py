money_available = 550
water_available = 400
milk_available = 540
coffee_available = 120
cups_available = 9


def print_status():
    print()
    print("The coffee machine has:")
    print(water_available, "of water")
    print(milk_available, "of milk")
    print(coffee_available, "of coffee beans")
    print(cups_available, "of disposable cups")
    print("${} of money".format(money_available))


def check_resources(qtd_water, qtd_milk, qtd_coffee, qtd_cups):
    global water_available
    global milk_available
    global coffee_available
    global cups_available

    if water_available < qtd_water:
        print("Sorry, not enough water!")
        return False
    elif milk_available < qtd_milk:
        print("Sorry, not enough milk!")
        return False
    elif coffee_available < qtd_coffee:
        print("Sorry, not enough coffee!")
        return False
    elif cups_available < qtd_cups:
        print("Sorry, not enough cups!")
        return False
    else:
        print("I have enough resources, making you a coffee!")
        return True


def make_espresso():
    global water_available
    global coffee_available
    global cups_available
    global money_available

    if check_resources(250, 0, 16, 1):
        water_available -= 250
        coffee_available -= 16
        cups_available -= 1
        money_available += 4


def make_latte():
    global water_available
    global milk_available
    global coffee_available
    global cups_available
    global money_available

    if check_resources(350, 75, 20, 1):
        water_available -= 350
        milk_available -= 75
        coffee_available -= 20
        cups_available -= 1
        money_available += 7


def make_cappuccino():
    global water_available
    global milk_available
    global coffee_available
    global cups_available
    global money_available

    if check_resources(200, 100, 12, 1):
        water_available -= 200
        milk_available -= 100
        coffee_available -= 12
        cups_available -= 1
        money_available += 6


def buy():
    type_id = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))
    if type_id == "1":
        make_espresso()
    elif type_id == "2":
        make_latte()
    elif type_id == "3":
        make_cappuccino()
    elif type_id == "back":
        pass
    else:
        print()
        print("Invalid option!")


def fill():
    global water_available
    global milk_available
    global coffee_available
    global cups_available
    print()
    water_available += int(input("Write how many ml of water do you want to add:"))
    milk_available += int(input("Write how many ml of milk do you want to add:"))
    coffee_available += int(input("Write how many grams of coffee beans do you want to add:"))
    cups_available += int(input("Write how many disposable cups of coffee do you want to add:"))


def take():
    global money_available
    print()
    print("I gave you $", money_available)
    money_available = 0

action = str()
while action != "exit":
    print()
    action = input("Write action (buy, fill, take, remaining, exit):")

    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        print_status()
    elif action == "exit":
        continue
    else:
        print("Invalid option!")

# cup_amount = int(input("How many cups of coffee you will need? "))

# print("For", cup_amount, "cups of coffee you will need:")
# print(cup_amount * 200, " ml of water")
# print(cup_amount * 50, " ml of milk")
# print(cup_amount * 15, " g of coffee beans")

# cups_available = min(int(water_available / 200), int(milk_available / 50), int(coffee_available / 15))

# if cups_available < cup_amount:
#     print("No, I can make only", cups_available, "cups of coffee")
# elif cups_available == cup_amount:
#     print("Yes, I can make that amount of coffee")
# elif cups_available > cup_amount:
#     print("Yes, I can make that amount of coffee (and even", cups_available - cup_amount, "more than that)")
