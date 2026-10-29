import csv

# Класс из ЛР №7
class Book:
    def __init__(self, title, author, year, price):
        self.__title = title
        self.__author = author
        self.__year = year
        if price < 0:
            self.__price = 0
        else:
            self.__price = price

    @property
    def title(self): return self.__title
    @property
    def author(self): return self.__author
    @property
    def year(self): return self.__year
    @property
    def price(self): return self.__price

    def display_info(self):
        print(f"'{self.__title}' ({self.__author}), {self.__year} г. - {round(self.__price, 2)} руб.")


# --- Сохранение в CSV ---
def save_to_csv(filename, books):
    # newline="" нужен, чтобы не было лишних пустых строк в CSV
    try:
        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            # Записываем заголовок
            writer.writerow(["Название", "Автор", "Год", "Цена"])
            # Записываем данные
            for b in books:
                writer.writerow([b.title, b.author, b.year, b.price])
        print(f"Данные сохранены в '{filename}'")
    except PermissionError:
        print(f"Ошибка: нет прав на запись в '{filename}'")
    except OSError as e:
        print(f"Ошибка при записи: {e}")


# --- Чтение из CSV ---
def load_from_csv(filename):
    books = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)  # пропускаем заголовок
            if header is None:
                print("Файл пустой.")
                return books

            for i, row in enumerate(reader, start=2):
                try:
                    # Преобразуем данные в нужные типы
                    title = row[0]
                    author = row[1]
                    year = int(row[2])
                    price = float(row[3])
                    books.append(Book(title, author, year, price))
                except (IndexError, ValueError) as e:
                    print(f"Ошибка в строке {i}: некорректные данные ({e})")
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
    except PermissionError:
        print(f"Ошибка: нет прав на чтение '{filename}'.")
    except csv.Error as e:
        print(f"Ошибка формата CSV: {e}")
    
    return books


# --- Главное меню ---
def main():
    filename = "books.csv"
    biblioteka = []

    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Добавить книгу")
        print("2 - Показать все книги")
        print("3 - Сохранить в CSV")
        print("4 - Загрузить из CSV")
        print("0 - Выход")
        choice = input("Выбор: ")

        if choice == "1":
            n = input("Название: ")
            a = input("Автор: ")
            try:
                g = int(input("Год: "))
                c = float(input("Цена: "))
                biblioteka.append(Book(n, a, g, c))
                print("Книга добавлена.")
            except ValueError:
                print("Ошибка: год должен быть целым, цена — числом.")

        elif choice == "2":
            if not biblioteka:
                print("Библиотека пуста.")
            else:
                for b in biblioteka:
                    b.display_info()

        elif choice == "3":
            save_to_csv(filename, biblioteka)

        elif choice == "4":
            loaded = load_from_csv(filename)
            if loaded:
                biblioteka = loaded
                print(f"Загружено книг: {len(biblioteka)}")

        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()