from cs50 import get_float

# 25 cents, 10 cents, 5 cents and 1 cent
change_owed = 0

while True:
    try:
        cash = get_float("Change: ")
        if cash >= 0:
            break
        else:
            print("Enter with a positive float number")
    except ValueError:
        print("Invalid input. Use a positive float number to enter")

cash *= 100

while cash > 0:
    if (cash // 25) > 0:
        cash -= 25
        change_owed += 1

    elif (cash // 10) > 0:
        cash -= 10
        change_owed += 1

    elif (cash // 5) > 0:
        cash -= 5
        change_owed += 1

    else:
        cash -= 1
        change_owed += 1

print(f"{change_owed}")
