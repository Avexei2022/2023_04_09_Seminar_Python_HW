def task_condition():
    print("\nЗадача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z. \n")

def print_result():
    print("X\tY\tZ\tF\n")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f"{x}\t{y}\t{z}\t{int(not (x and y) or z)}")


task_condition()
print_result()
