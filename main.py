def check_operator_forward_calc(user_input):
    if "+" in user_input:
        calc_result = calc_addition(user_input)
    elif "-" in user_input:
        calc_result = calc_subtraction(user_input)
    elif "*" in user_input:
        calc_result = calc_multiplication(user_input)
    elif "/" in user_input:
        calc_result = calc_division(user_input)
    elif "~" in user_input:
        calc_result = calc_floor_division_modulo(user_input)
    else:
        return "not possible due to an invalid operator, please try again.", None
    return calc_result


def calc_addition(user_input):
    num1, num2 = user_input.split("+")
    return int(num1) + int(num2), None


def calc_subtraction(user_input):
    num1, num2 = user_input.split("-")
    return int(num1) - int(num2), None


def calc_multiplication(user_input):
    num1, num2 = user_input.split("*")
    return int(num1) * int(num2), None


def calc_division(user_input):
    num1, num2 = user_input.split("/")
    num1 = int(num1)
    num2 = int(num2)
    if num2 == 0:
        return "not possible due to an attempt to perform division by zero, please try again.", None
    return round(num1 / num2, 2), None


def calc_floor_division_modulo(user_input):
    num1, num2 = user_input.split("~")
    num1 = int(num1)
    num2 = int(num2)
    if num2 == 0:
        return "not possible due to an attempt to perform floor division by zero, please try again.", None
    return num1 // num2, num1 % num2


def print_result(calc_result):
    print(f"The answer is {calc_result[0]}")
    if calc_result[1] is not None:
        print(f"The remainder is {calc_result[1]}")


def main():
    print("Welcome to the Python calculator!")
    calculation_cycles = int(input("How many calculations do you want to do? "))
    for cycle in range(calculation_cycles):
        user_input = input("What do you want to calculate? ")
        calc_result = check_operator_forward_calc(user_input)
        print_result(calc_result)
    print("Thank you for using the Python calculator!")


if __name__ == "__main__":
    main()