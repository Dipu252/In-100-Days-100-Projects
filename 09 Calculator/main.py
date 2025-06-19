import art

print(art.logo)

def add(n1, n2):
    return n1 + n2


def substraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1/n2

function = {
    "+": add,
    "-" : substraction,
    "*" : multiplication,
    "/" : division
}

num1 = float(input("What is the first number?: "))

should_accumulate = True

while should_accumulate:
    for operator in function:
        print(operator)
    operation = input("Pick an operation: ")

    if operation not in function:
        print("Pick valid operation!")
        continue

    num2 = float(input("What is the next number?: "))
    answer = function[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")

    choice = input(f"Type 'y' to continue calcutation with {answer}. Type 'n' to start new calcutation: ")

    if choice == 'y':
        num1=answer
    else:
        should_accumulate = False


