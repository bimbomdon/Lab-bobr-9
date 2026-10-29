import json
import xml.etree.ElementTree as ET

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


# --- Сериализация в JSON ---
def save_json(book, filename):
    try:
        # Превращаем объект в словарь
        data = {
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "price": book.price
        }
        # Записываем в файл с отступами для читаемости
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Книга сохранена в JSON: '{filename}'")
    except PermissionError:
        print(f"Ошибка: нет прав на запись в '{filename}'")
    except OSError as e:
        print(f"Ошибка записи: {e}")


# --- Десериализация из JSON ---
def load_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Создаём объект из словаря
        book = Book(
            data["title"],
            data["author"],
            data["year"],
            data["price"]
        )
        print(f"Книга загружена из JSON: '{filename}'")
        return book
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
    except PermissionError:
        print(f"Ошибка: нет прав на чтение '{filename}'.")
    except json.JSONDecodeError:
        print(f"Ошибка: файл '{filename}' содержит некорректный JSON.")
    except KeyError as e:
        print(f"Ошибка: в JSON не хватает поля {e}.")
    except (ValueError, TypeError) as e:
        print(f"Ошибка данных в JSON: {e}")
    return None


# --- Сериализация в XML ---
def save_xml(book, filename):
    try:
        # Создаём корневой элемент
        root = ET.Element("book")
        
        # Добавляем дочерние элементы
        ET.SubElement(root, "title").text = book.title
        ET.SubElement(root, "author").text = book.author
        ET.SubElement(root, "year").text = str(book.year)
        ET.SubElement(root, "price").text = str(book.price)

        # Создаём дерево и записываем
        tree = ET.ElementTree(root)
        # Для отступов и читаемости (доступно с Python 3.9)
        ET.indent(tree, space="    ")
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            tree.write(f, encoding="unicode")
        
        print(f"Книга сохранена в XML: '{filename}'")
    except PermissionError:
        print(f"Ошибка: нет прав на запись в '{filename}'")
    except OSError as e:
        print(f"Ошибка записи: {e}")


# --- Десериализация из XML ---
def load_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        title = root.find("title").text
        author = root.find("author").text
        year = int(root.find("year").text)
        price = float(root.find("price").text)

        book = Book(title, author, year, price)
        print(f"Книга загружена из XML: '{filename}'")
        return book
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
    except PermissionError:
        print(f"Ошибка: нет прав на чтение '{filename}'.")
    except ET.ParseError:
        print(f"Ошибка: файл '{filename}' содержит некорректный XML.")
    except AttributeError:
        print(f"Ошибка: в XML не хватает нужных тегов.")
    except (ValueError, TypeError) as e:
        print(f"Ошибка данных в XML: {e}")
    return None


# --- Главное меню ---
def main():
    book = Book("Война и мир", "Лев Толстой", 1869, 1500.0)
    
    print("Исходная книга:")
    book.display_info()

    # JSON
    print("\n--- JSON ---")
    save_json(book, "book.json")
    loaded_json = load_json("book.json")
    if loaded_json:
        loaded_json.display_info()

    # XML
    print("\n--- XML ---")
    save_xml(book, "book.xml")
    loaded_xml = load_xml("book.xml")
    if loaded_xml:
        loaded_xml.display_info()


if __name__ == "__main__":
    main()