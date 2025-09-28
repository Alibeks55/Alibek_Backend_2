import sqlite3

conn = sqlite3.connect('books_genres.db')

def create_genres_table():
    conn.execute('DROP TABLE IF EXISTS genres')
    conn.execute('''
        CREATE TABLE genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')
    conn.commit()

def create_books_table():
    conn.execute('DROP TABLE IF EXISTS books')
    conn.execute('''
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            number_of_pages INTEGER,
            number_of_copies INTEGER,
            genre_id INTEGER,
            price REAL,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    ''')
    conn.commit()

def insert_books():
    conn.executemany(
        'INSERT INTO books (name, author, publication_year, number_of_pages, number_of_copies, genre_id, price) VALUES (?,?,?,?,?,?,?)',
        [
            ('Гарри Поттер', 'Дж. К. Роулинг', 1997, 320, 10, 1,500),
            ('Шерлок Холмс', 'Артур Конан Дойл', 1892, 450, 9, 2,700),
            ('Война и мир', 'Л. Н. Толстой', 1869, 1225, 5, 3,1200),
            ('Маленький принц', 'А. де Сент-Экзюпери', 1943, 96, 15, 4,200),
            ('Грузовой перевал', 'Дж. С. Джексон', 1950, 512, 3, 5,600),
            ('Братья Карамазовы', 'Ф. М. Достоевский', 1880, 824, 6, 3,650),
            ('Герой нашего времени', 'М. Ю. Лермонтов', 1840, 224, 8, 3,800)
        ]
    )
    conn.commit()

def insert_genres():
    conn.executemany(
        'INSERT INTO genres (name) VALUES (?)',
        [
            ('Фэнтези',),
            ('Детектив',),
            ('Роман',),
            ('Сказка',),
            ('Приключения',)
        ]
    )
    conn.commit()

def get_all_books():
    print('-------Все книги-------')
    cursor = conn.execute('''
        SELECT b.id, b.name, b.author, g.name AS genre, b.price
        FROM books b
        JOIN genres g ON b.genre_id = g.id
    ''')
    for cur in cursor:
        print(cur)

def filter_books_by_genre_name(genre: str):
    print(f'\n-------Книги жанра: "{genre}"-------')
    cursor = conn.execute('''
        SELECT b.id, b.name, b.author, g.name AS genre
        FROM books b
        JOIN genres g ON b.genre_id = g.id
        WHERE g.name = ?
    ''', (genre,))

    for cur in cursor:
        print(cur)

def filter_genres_by_book_price(low: int, high: int):
    print(f'\n-------Жанры книг с ценой между {low} и {high}-------')
    cursor = conn.execute('''
        SELECT DISTINCT g.name 
        FROM books b
        JOIN genres g ON b.genre_id = g.id
        WHERE b.price BETWEEN ? AND ?
    ''',(low,high))

    for cur in cursor:
        print(cur)


if __name__ == "__main__":

 create_genres_table()
 create_books_table()
 insert_genres()
 insert_books()
 get_all_books()
 filter_books_by_genre_name('Роман')
 filter_genres_by_book_price(600,700)

 conn.close()

