def task_condition():
    print("\nЗадача 4. Задайте список из N элементов, заполненных числами из промежутка[-N, N].\n"
          "Сдвиньте все элементы списка на 2 позиции вправо.\n"
           "3 -> [2, 3, -3, -2, -1, 0, 1]\n")
    

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
        if number > 0:
            check_input = False
        else:
            print(f"{number} -> Число не натуральное.")
    return number

def get_list(number):
    list_n = []
    for i in range(-number, number + 1):
        list_n.append(int(i))
    return list_n

def get_changed_list(list_n, shift_num):
    last_index = len(list_n) - 1
    for i in range(shift_num):
        temp_value = list_n[last_index]
        for j in range(last_index, 0, -1):
            list_n[j] = list_n[j - 1]
        list_n[0] = temp_value
    return list_n

def print_result(message, number, list_n):
    print(f"Cписок от {-number} до {number} {message} -> {list_n}")

task_condition()
number = get_number("Введите натуральное число N: ")
list_n = get_list(number)
print_result("исходный", number, list_n)
shift_num = get_number("Введите количество позиций смещения вправо (по условиям задачи 2): ")
get_changed_list(list_n, shift_num)
print_result(f"со сдвигом на {shift_num} позиции вправо", number, list_n)
