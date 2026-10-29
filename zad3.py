import os

# Функция для подсчёта статистики в файле
def analyze_file(filename):
    # Пытаемся открыть файл на чтение
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return None
    except PermissionError:
        print(f"Ошибка: нет доступа к файлу '{filename}'.")
        return None
    except UnicodeDecodeError:
        print(f"Ошибка: файл '{filename}' содержит символы, которые нельзя прочитать в UTF-8.")
        return None

    # Подсчёт символов (включая пробелы и переносы строк)
    char_count = len(text)
    
    # Подсчёт строк
    lines = text.splitlines()
    line_count = len(lines)
    
    # Подсчёт слов (разбиваем по пробелам)
    words = text.split()
    word_count = len(words)

    return char_count, line_count, word_count, text


# Функция для копирования файла
def copy_file(source, destination):
    # Читаем исходный файл
    data = analyze_file(source)
    if data is None:
        return # если чтение не удалось, выходим

    char_count, line_count, word_count, text = data

    # Пытаемся записать в новый файл
    try:
        with open(destination, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Файл успешно скопирован в '{destination}'.")
    except PermissionError:
        print(f"Ошибка: нет прав на запись в файл '{destination}'.")
        return
    except OSError as e:
        print(f"Ошибка при записи: {e}")
        return

    # Выводим статистику
    print("\n--- Статистика ---")
    print(f"Строк: {line_count}")
    print(f"Слов: {word_count}")
    print(f"Символов (включая пробелы): {char_count}")


# Главный цикл программы
def main():
    print("Копирование файла с подсчётом статистики")
    
    source = input("Введите имя исходного файла: ")
    destination = input("Введите имя файла для копии: ")

    copy_file(source, destination)


if __name__ == "__main__":
    main()