# =================================================================
#                     NEW VERSION 13.07.25
# =================================================================
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
    print(" " * spaces + "#" * bricks)

# =================================================================
#                     OLD VERSION 12.07.25
# =================================================================
# while True:
#     h = input("Height: ")
#     try:
#         if h.isnumeric() and (int(h) > 0 and int(h) <= 8):
#             break
#         elif h.isnumeric() and int(h) > 8:
#             h = input("Height: ")
#             break
#         else:
#             h = input("Height: ")
#     except ValueError:
#         print("Not numeric")

# for i in range(int(h)):
#     for j in range(int(h)):
#         if j >= (int(h) - i - 1):
#             print("#", end="")

#         else:
#             print(" ", end="")
#     print()
