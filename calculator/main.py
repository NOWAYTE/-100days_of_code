# calculator

# addition
def add(n1, n2):
    return n1 + n2


# subtraction
def sub(n1, n2):
    return n1 - n2


# multiplication
def mul(n1, n2):
    return n1 * n2


# division
def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def cal():
    from art import logo

    print(logo)
    num1 = float(input("input your first number"))

    for operator in operations:
        print(operator)
    should_continue = False

    while not should_continue:
        operator = input("pick an operator")
        num2 = float(input("pick a number"))
        calculation_functions = operations[operator]
        first_answer = calculation_functions(num1, num2)
        print(f"{num1} {operator} {num2} = {first_answer}")

        game_continue = input("do you want to continue ? type y for yes and n to start over  ").lower()

        if game_continue == "y":
            num1 = first_answer

        else:
            should_continue = True
            print(f"{num1} {operator} {num2} = {first_answer}")
            cal()


cal()
