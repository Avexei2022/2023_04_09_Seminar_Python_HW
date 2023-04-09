def task_condition():
    print("\nЗадача 1. Напишите программу, которая принимает на вход число N\n"
          "и выдает список факториалов для чисел от 1 до N.\n"
          "пусть N=4 -> [1, 2, 6, 24](1, 1*2, 1*2*3, 1*2*3*4)\n")

def get_integer(message):
    check_int = True
    while check_int:
        try:
            number = int(input())
            check_int = False
        except:
            print(
                f"Условия ввода не выполнены.\n{message}", end=' ')
    return number


def get_number(message):
    check_input = True
    while check_input:
        print(f"{message} ", end='')
        number = get_integer(message)
        if number > 0 and number < 21:
            check_input = False
        else:
            print(f"{number} -> Условия ввода не выполнены.")
    return number

def get_factorial(number):
    factorial_list = []
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
        factorial_list.append(factorial)
    return factorial_list

def print_factorial_list(number):
    print(f"N = {number} -> {get_factorial(number)}")
    for i in range(1, number + 1):
        print(f"{i} -> {get_factorial(i)}")
    print(f"")

task_condition()
number = get_number("Введите натуральное число N (1-20): ")
print_factorial_list(number)
