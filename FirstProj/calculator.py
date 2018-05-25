# used to sum
def add(num1, num2):
    return num1 + num2


# used for mul
def sub(num1, num2):
    return num1 - num2


# used for mul
def mul(num1, num2):
    return num1 * num2


# used for mul
def div(num1, num2):
    return num1 / num2


def main():
    num1 = int(input('enter ur first number'))
    num2 = int(input('enter ur second number'))

    operation = int(input("what u want to perform? 1.add - 2.subtract 3.multiply 4.divide"))
    if (operation == 1):
        print("Adding...")
        print(add(num1, num2))
    elif (operation == 2):
        print("Subtracting...")
        print(sub(num1, num2))
    elif( operation ==3):
        print("Multiplying...")
        print(mul(num1, num2))
    else:
        print("Dividing...")
        print(div(num1, num2))


main()