# Программа: читает файл, считает частоту слов,
# сортирует по убыванию и записывает результат в result.txt

def count_words(filename):
    """Читает файл и возвращает словарь {слово: количество}."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return None
    except PermissionError:
        print(f"Ошибка: нет прав на чтение файла '{filename}'.")
        return None
    except UnicodeDecodeError:
        print(f"Ошибка: файл '{filename}' не в кодировке UTF-8.")
        return None

    # Приводим к нижнему регистру и убираем знаки препинания (простая замена)
    text = text.lower()
    # Заменяем все не-буквы и не-цифры на пробелы
    cleaned = ""
    for ch in text:
        if ch.isalnum() or ch.isspace():
            cleaned += ch
        else:
            cleaned += " "

    words = cleaned.split()

    # Считаем частоту
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


def save_result(filename, freq):
    """Сортирует словарь и записывает в файл."""
    if not freq:
        print("Нет данных для записи.")
        return

    # Сортируем: сначала по частоте (по убыванию), потом по алфавиту
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Слово\tКоличество\n")
            f.write("-" * 30 + "\n")
            for word, count in sorted_words:
                f.write(f"{word}\t{count}\n")
        print(f"Результат записан в '{filename}'.")
    except PermissionError:
        print(f"Ошибка: нет прав на запись в файл '{filename}'.")
    except OSError as e:
        print(f"Ошибка записи: {e}")


def main():
    source = input("Имя файла для анализа: ")
    freq = count_words(source)
    
    if freq is not None:
        if len(freq) == 0:
            print("В файле не найдено слов.")
        else:
            save_result("result.txt", freq)


if __name__ == "__main__":
    main()