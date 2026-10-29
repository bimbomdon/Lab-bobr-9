import re

def validate_email(email):
    """Простая проверка email через регулярное выражение."""
    # Что-то@что-то.что-то
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Проверка телефона (российский формат)."""
    # Допускаем: +7XXXXXXXXXX, 8XXXXXXXXXX, с пробелами, дефисами или скобками
    pattern = r'^(\+7|8)[\s\-\(\)]*\d{3}[\s\-\(\)]*\d{3}[\s\-]*\d{2}[\s\-]*\d{2}$'
    return re.match(pattern, phone) is not None

def check_file(filename):
    """Читает файл и проверяет каждую строку."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return
    except PermissionError:
        print(f"Ошибка: нет прав на чтение файла '{filename}'.")
        return
    except UnicodeDecodeError:
        print(f"Ошибка: файл '{filename}' не в кодировке UTF-8.")
        return

    errors = 0
    total = 0

    print(f"\n--- Проверка файла '{filename}' ---")
    
    for i, line in enumerate(lines, start=1):
        text = line.strip()
        if not text:
            continue # Пропускаем пустые строки
        
        total += 1
        
        # Если в строке есть '@', проверяем как email
        if "@" in text:
            if not validate_email(text):
                print(f"Строка {i}: Некорректный email -> '{text}'")
                errors += 1
        # Иначе проверяем как телефон
        else:
            if not validate_phone(text):
                print(f"Строка {i}: Некорректный телефон -> '{text}'")
                errors += 1

    print("-" * 30)
    print(f"Всего проверено строк: {total}")
    print(f"Найдено ошибок: {errors}")

def main():
    filename = input("Введите имя файла для проверки: ")
    check_file(filename)

if __name__ == "__main__":
    main()