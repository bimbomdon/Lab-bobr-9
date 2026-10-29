# Программа: записывает массив чисел в файл, читает его обратно,
# считает сумму и среднее. Обрабатывает ошибки (файл не найден и др.)

def write_array(filename, array):
    # Открываем файл на запись. with закроет его автоматически.
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for num in array:
                f.write(str(num) + "\n")
        print("Массив записан в файл", filename)
    except PermissionError:
        print("Ошибка: нет прав на запись в файл", filename)
    except OSError as e:
        print("Ошибка при записи файла:", e)


def read_array(filename):
    # Открываем файл на чтение
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        # Это и есть FileNotFoundException
        print("Ошибка: файл", filename, "не найден!")
        return None
    except PermissionError:
        print("Ошибка: нет прав на чтение файла", filename)
        return None

    # Преобразуем строки в числа
    array = []
    for i, line in enumerate(lines, start=1):
        line = line.strip()
        if line == "":
            continue
        try:
            array.append(float(line))
        except ValueError:
            print(f"Ошибка в строке {i}: '{line}' — это не число")
            return None
    return array


# Главная часть
filename = "numbers.txt"

# Ввод чисел
user_input = input("Введите числа через пробел: ")
try:
    numbers = [float(x) for x in user_input.split()]
except ValueError:
    print("Ошибка: вы ввели не числа.")
    numbers = []

# Если числа есть — записываем
if numbers:
    write_array(filename, numbers)

# Читаем массив из файла
data = read_array(filename)

# Если прочиталось — считаем сумму и среднее
if data:
    total = sum(data)
    average = total / len(data)
    print("Прочитанный массив:", data)
    print("Сумма:", total)
    print("Среднее:", round(average, 2))
elif data == []:
    print("Файл пустой, считать нечего.")