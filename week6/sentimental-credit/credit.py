from cs50 import get_int, get_string

credit_num = get_int("Number: ")
copy_credit_num = credit_num
s_credit_num = str(credit_num)

size = len(s_credit_num)
first_num = credit_num // 10 ** (size - 1)
second_num = credit_num // 10 ** (size - 2)

luhn = 0

for i in range(size):

    digit = credit_num % 10
    credit_num = credit_num // 10

    if i % 2 == 1:
        product = digit * 2

        if product > 9:
            luhn += product // 10 + product % 10

        else:
            luhn += product

    else:
        luhn += digit

if luhn % 10 == 0:
    if (second_num == 34 or second_num == 37) and size == 15:
        print("AMEX")

    elif (51 <= second_num <= 55) and size == 16:
        print("MASTERCARD")

    elif first_num == 4 and (size == 13 or size == 16):
        print("VISA")

    else:
        print("INVALID")

else:
    print("INVALID")
