import os

def merge_files(output_file, input_files):
    """Объединяет несколько файлов в один."""
    try:
        with open(output_file, "wb") as outfile:
            for filename in input_files:
                # Открываем каждый файл в бинарном режиме для чтения
                with open(filename, "rb") as infile:
                    # Читаем данные и записываем в общий файл
                    outfile.write(infile.read())
        print(f"Файлы успешно объединены в '{output_file}'.")
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден -> {e.filename}")
    except PermissionError:
        print("Ошибка: нет прав на чтение или запись.")
    except OSError as e:
        print(f"Ошибка ввода-вывода: {e}")


def split_file(source_file, part_size, output_prefix):
    """Разделяет файл на части заданного размера (в байтах)."""
    try:
        # Проверяем, существует ли файл
        if not os.path.exists(source_file):
            raise FileNotFoundError(f"Файл '{source_file}' не найден.")
        
        # Проверяем, что размер части больше нуля
        if part_size <= 0:
            raise ValueError("Размер части должен быть больше 0.")

        part_num = 1
        with open(source_file, "rb") as infile:
            while True:
                # Читаем кусок файла
                chunk = infile.read(part_size)
                if not chunk:
                    break  # Дошли до конца файла
                
                # Формируем имя для новой части
                part_name = f"{output_prefix}_part{part_num}.dat"
                
                # Записываем кусок в отдельный файл
                with open(part_name, "wb") as outfile:
                    outfile.write(chunk)
                
                print(f"Создан файл: '{part_name}' (размер: {len(chunk)} байт)")
                part_num += 1
                
        print(f"Файл '{source_file}' успешно разделён на {part_num - 1} частей.")
        
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
    except PermissionError:
        print("Ошибка: нет прав на чтение исходного или запись новых файлов.")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except OSError as e:
        print(f"Ошибка ввода-вывода: {e}")


def main():
    while True:
        print("\n--- АРХИВАТОР ---")
        print("1 - Объединить файлы")
        print("2 - Разделить файл")
        print("0 - Выход")
        choice = input("Выбор: ")

        if choice == "1":
            # Ввод списка файлов
            files_input = input("Введите имена файлов через запятую: ")
            files_list = [f.strip() for f in files_input.split(",") if f.strip()]
            
            if not files_list:
                print("Вы не выбрали ни одного файла.")
                continue
                
            output_name = input("Имя итогового файла: ")
            merge_files(output_name, files_list)

        elif choice == "2":
            source = input("Какой файл разделить? ")
            try:
                size = int(input("Размер одной части (в байтах): "))
            except ValueError:
                print("Ошибка: размер должен быть целым числом.")
                continue
                
            prefix = input("Префикс для новых файлов (например, 'part'): ")
            split_file(source, size, prefix)

        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()