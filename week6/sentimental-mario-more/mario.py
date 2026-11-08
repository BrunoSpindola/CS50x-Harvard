while True:
    try:
        h = int(input("Height: "))
        if 1 <= h <= 8:
            break
        else:
            print("Height must be between 1 and 8")
    except ValueError:
        print("Invalid input. Please enter a number.")

for i in range(h):
    spaces = h - i - 1
    bricks = i + 1
    print(" " * spaces + "#" * bricks + "  " + "#" * bricks, end="\n")
