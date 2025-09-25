import sqlite3

conn = sqlite3.connect("database.db")

def create_table():
    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("""
        CREATE TABLE books (
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER,
            deleted INTEGER DEFAULT 0
        )
    """)

def books_archive():
    conn.execute("DROP TABLE IF EXISTS books_archive")
    conn.execute("""
        CREATE TABLE books_archive (
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

def insert_books():
    conn.executemany(
        "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) "
         "VALUES (?, ?, ?, ?, ?, ?) ",
        [
        ("Гарри Поттер", "Дж. К. Роулинг", 1997, "Фэнтези", 320, 10),
        ("Шерлок Холмс", "Артур Конан Дойл", 1892, "Детектив", 450, 9),
        ("Война и мир", "Л. Н. Толстой", 1869, "Роман", 1225, 5),
        ("Мертвые души", "Н. В. Гоголь", 1842, "Роман", 432, 6),
        ("Преступление и наказание", "Ф. М. Достоевский", 1866, "Роман", 671, 7),
        ("Маленький принц", "А. де Сент-Экзюпери", 1943, "Сказка", 96, 15),
        ("Унесённые ветром", "М. Митчелл", 1936, "Роман", 1037, 4),
        ("Братья Карамазовы", "Ф. М. Достоевский", 1880, "Роман", 824, 6),
        ("Грузовой перевал", "Дж. С. Джексон", 1950, "Приключения", 512, 3),
        ("Герой нашего времени", "М. Ю. Лермонтов", 1840, "Роман", 224, 8)]
    )
    conn.commit()

def soft_delete(name):
    conn.execute("""
        INSERT INTO books_archive (name, author, publication_year, genre, number_of_pages, number_of_copies)
        SELECT name, author, publication_year, genre, number_of_pages, number_of_copies
        FROM books
        WHERE name = ? AND deleted = 0
    """, (name,))
    conn.commit()

    conn.execute("UPDATE books SET deleted = 1 WHERE name = ?", (name,))
    conn.commit()

def hard_delete(name):
    conn.execute("DELETE FROM books WHERE name = ? AND deleted = 1", (name,))
    conn.commit()

if __name__ == "__main__":
    create_table()
    books_archive()
    insert_books()

    soft_delete("Унесённые ветром")
    soft_delete("Мертвые души")
    hard_delete("Мертвые души")

    conn.close()