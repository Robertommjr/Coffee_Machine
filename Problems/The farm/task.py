money = int(input())

CHICKEN_PRICE: int = 23
GOAT_PRICE: int = 678
PIG_PRICE: int = 1296
COW_PRICE: int = 3848
SHEEP_PRICE: int = 6769

if money >= SHEEP_PRICE:
    print(int(money / SHEEP_PRICE), "sheep")
elif money >= COW_PRICE:
    qtd = int(money / COW_PRICE)
    print(qtd, "cows" if qtd > 1 else "cow")
elif money >= PIG_PRICE:
    qtd = int(money / PIG_PRICE)
    print(qtd, "pigs" if qtd > 1 else "pig")
elif money >= GOAT_PRICE:
    qtd = int(money / GOAT_PRICE)
    print(qtd, "goats" if qtd > 1 else "goat")
elif money >= CHICKEN_PRICE:
    qtd = int(money / CHICKEN_PRICE)
    print(qtd, "chickens" if qtd > 1 else "chicken")
else:
    print("None")
