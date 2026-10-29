import os

# Файл дневника
FILENAME = "diary.txt"

# 1. Добавление записи в дневник
def add_entry(date, text):
    # Открываем файл в режиме добавления (если файла нет — создастся)
    with open(FILENAME, "a", encoding="utf-8") as f:
        # Записываем в формате: [дата] текст
        f.write(f"[{date}] {text}\n")
    print("Запись добавлена в дневник.")

# 2. Вывод всех записей
def show_all():
    # Проверяем, существует ли файл
    if not os.path.exists(FILENAME):
        print("Дневник пуст (файл не найден).")
        return

    # Открываем и читаем
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if len(lines) == 0:
        print("Дневник пуст.")
    else:
        print("\n--- ВСЕ ЗАПИСИ ---")
        for line in lines:
            print(line.strip())

# 3. Поиск по дате
def search_by_date(date):
    if not os.path.exists(FILENAME):
        print("Файл дневника не найден.")
        return

    found = False
    with open(FILENAME, "r", encoding="utf-8") as f:
        for line in f:
            # Ищем строки, которые начинаются с нужной даты в скобках
            if line.startswith(f"[{date}]"):
                print(line.strip())
                found = True

    if not found:
        print(f"Записей за {date} не найдено.")


# Главный цикл программы
def main():
    while True:
        print("\n--- ДНЕВНИК ---")
        print("1 - Добавить запись")
        print("2 - Показать все записи")
        print("3 - Найти по дате")
        print("0 - Выход")
        choice = input("Выбор: ")

        if choice == "1":
            date = input("Введите дату (например, 12.05.2024): ")
            text = input("Введите текст записи: ")
            
            # Запись в файл с обработкой ошибок
            try:
                add_entry(date, text)
            except PermissionError:
                print("Ошибка: нет прав на запись в файл.")
            except OSError as e:
                print("Ошибка ввода-вывода:", e)

        elif choice == "2":
            try:
                show_all()
            except PermissionError:
                print("Ошибка: нет прав на чтение файла.")
            except OSError as e:
                print("Ошибка ввода-вывода:", e)

        elif choice == "3":
            date = input("Какую дату искать? ")
            try:
                search_by_date(date)
            except PermissionError:
                print("Ошибка: нет прав на чтение файла.")
            except OSError as e:
                print("Ошибка ввода-вывода:", e)

        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Нет такого пункта меню.")


if __name__ == "__main__":
    main()