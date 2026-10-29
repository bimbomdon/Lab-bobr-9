import os

# Простой шифр Цезаря (сдвиг по ASCII)
def encrypt(text, key):
    result = ""
    for char in text:
        # Сдвигаем каждый символ на key позиций вперёд
        result += chr(ord(char) + key)
    return result

def decrypt(text, key):
    result = ""
    for char in text:
        # Сдвигаем каждый символ на key позиций назад
        result += chr(ord(char) - key)
    return result


# Шифрование файла
def encrypt_file(source, destination, key):
    try:
        # Читаем исходный файл
        with open(source, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Шифруем
        encrypted_text = encrypt(text, key)
        
        # Записываем в новый файл
        with open(destination, "w", encoding="utf-8") as f:
            f.write(encrypted_text)
        
        print(f"Файл '{source}' зашифрован и сохранён как '{destination}'.")
        
    except FileNotFoundError:
        print(f"Ошибка: файл '{source}' не найден.")
    except PermissionError:
        print(f"Ошибка: нет прав на чтение '{source}' или запись в '{destination}'.")
    except UnicodeDecodeError:
        print(f"Ошибка: файл '{source}' не в кодировке UTF-8.")
    except OSError as e:
        print(f"Ошибка ввода-вывода: {e}")


# Расшифровка файла
def decrypt_file(source, destination, key):
    try:
        # Читаем зашифрованный файл
        with open(source, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Расшифровываем
        decrypted_text = decrypt(text, key)
        
        # Записываем расшифрованный текст
        with open(destination, "w", encoding="utf-8") as f:
            f.write(decrypted_text)
        
        print(f"Файл '{source}' расшифрован и сохранён как '{destination}'.")
        
    except FileNotFoundError:
        print(f"Ошибка: файл '{source}' не найден.")
    except PermissionError:
        print(f"Ошибка: нет прав на чтение '{source}' или запись в '{destination}'.")
    except UnicodeDecodeError:
        print(f"Ошибка: файл '{source}' не в кодировке UTF-8.")
    except OSError as e:
        print(f"Ошибка ввода-вывода: {e}")


# Главный цикл
def main():
    print("Шифрование и дешифрование файла (шифр Цезаря)")
    
    while True:
        print("\n1 - Зашифровать файл")
        print("2 - Расшифровать файл")
        print("0 - Выход")
        choice = input("Выбор: ")

        if choice == "1":
            src = input("Имя исходного файла: ")
            dst = input("Имя файла для зашифрованного текста: ")
            
            try:
                key = int(input("Ключ шифрования (целое число): "))
            except ValueError:
                print("Ошибка: ключ должен быть целым числом.")
                continue

            encrypt_file(src, dst, key)

        elif choice == "2":
            src = input("Имя зашифрованного файла: ")
            dst = input("Имя файла для расшифрованного текста: ")
            
            try:
                key = int(input("Ключ шифрования (целое число): "))
            except ValueError:
                print("Ошибка: ключ должен быть целым числом.")
                continue

            decrypt_file(src, dst, key)

        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()