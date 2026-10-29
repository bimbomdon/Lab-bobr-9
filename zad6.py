import os

# Файл для лога
LOG_FILE = "log.txt"

def write_log(message):
    # Открываем файл в режиме добавления, чтобы не стирать старые записи
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    except PermissionError:
        print(f"Не удалось записать лог: нет прав на файл {LOG_FILE}")
    except OSError as e:
        print("Ошибка записи лога:", e)


def calculate(a, b, operation):
    """Выполняет операцию и возвращает результат."""
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        # Обработка деления на ноль
        if b == 0:
            raise ZeroDivisionError("Деление на ноль!")
        return a / b
    else:
        raise ValueError("Неизвестная операция")


def main():
    while True:
        print("\n--- КАЛЬКУЛЯТОР ---")
        print("Введите выражение в формате: число операция число")
        print("Например: 5 + 3 или 10 / 2 (или 0 для выхода)")
        
        user_input = input("Ввод: ").strip()

        if user_input == "0":
            print("Выход.")
            break

        # Разбиваем строку на части
        parts = user_input.split()
        if len(parts) != 3:
            print("Ошибка: нужно ввести ровно 3 части (число, операция, число).")
            continue

        num1_str, op, num2_str = parts

        try:
            # Преобразуем в числа
            a = float(num1_str)
            b = float(num2_str)

            # Выполняем операцию
            result = calculate(a, b, op)
            print(f"Результат: {a} {op} {b} = {result}")

            # Записываем в лог успешную операцию
            write_log(f"УСПЕХ: {a} {op} {b} = {result}")

        except ValueError as e:
            print("Ошибка: введите корректные числа или операцию.")
            write_log(f"ОШИБКА ВВОДА: '{user_input}' ({e})")
            
        except ZeroDivisionError as e:
            print("Ошибка:", e)
            write_log(f"ОШИБКА ДЕЛЕНИЯ: '{user_input}' (деление на ноль)")
            
        except Exception as e:
            # На случай других непредвиденных ошибок
            print("Что-то пошло не так:", e)
            write_log(f"НЕИЗВЕСТНАЯ ОШИБКА: '{user_input}' ({e})")


if __name__ == "__main__":
    main()