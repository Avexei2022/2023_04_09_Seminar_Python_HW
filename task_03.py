def task_condition():
    print("\nЗадача 3. Даны две строки.\n"
          "Посчитайте сколько раз каждый символ первой строки встречается во второй\n"
          "«one» «onetwonine» - o – 2, n – 3, e – 2\n")
    
def get_string(sring_num):
    string = input(f"Введите строку {sring_num}: ")
    return string

def get_result(string_1, string_2):
    result = []
    for i in range(len(string_1)):
        count = 0
        for j in range(len(string_2)):
            if string_2[j] == string_1[i]:
                count += 1
        result.append(count)
    return result

def print_result(string1, string_2, result):
    print(f'"{string_1}" "{string_2}"', end=' - ')
    for i in range(len(string_1)):
        print(f" {string_1[i]} - {result[i]}", end=' ')

task_condition()
string_1 = get_string("1")
string_2 = get_string("2")
result = get_result(string_1, string_2)
print_result(string_1, string_2, result)
