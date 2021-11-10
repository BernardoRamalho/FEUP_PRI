import csv
import sqlite3
from sqlite3.dbapi2 import connect
import sys

csv.field_size_limit(sys.maxsize)
    
connection = sqlite3.connect('books.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS book')
cursor.execute('''
    CREATE TABLE book(
        book_id INTEGER PRIMARY KEY NOT NULL,
        bookformat TEXT NOT NULL,
        desc TEXT NOT NULL,
        img TEXT NOT NULL,
        isbn TEXT NOT NULL,
        link TEXT NOT NULL UNIQUE,
        pages INTEGER NOT NULL,
        reviews INTEGER NOT NULL,
        title TEXT NOT NULL,
        rating REAL,
        totalratings INTEGER
    )
''')


print("#################################")
print("#       Processing books        #")
print("#################################")
print()

with open('books.csv') as books_csv:
    csv_reader = csv.reader(books_csv, delimiter=',')
    next(csv_reader, None)
    i = 0
    for row in csv_reader:
        print('Processing row {} of 99999'.format(i), end="\r")
        i += 1
        book_id = int(row[0])
        bookformat = row[1]
        desc = row[2]
        img = row[3]
        isbn = row[4]
        link = row[5]
        pages = int(row[6])
        reviews = int(row[7])
        title = row[8]
        cursor.execute('''
            INSERT INTO book(book_id,bookformat,desc,img,isbn,link,pages,reviews,title)
            VALUES (?,?,?,?,?,?,?,?,?)
        ''', (book_id, bookformat, desc,img,isbn,link,pages,reviews,title))
    connection.commit()

print("#################################")
print("#      Processing ratings       #")
print("#################################")
print()

with open('ratings.csv') as ratings_csv:
    csv_reader = csv.reader(ratings_csv, delimiter=',')
    next(csv_reader, None)
    i = 0
    for row in csv_reader:
        print('Processing row {} of 99999'.format(i), end="\r")
        i += 1
        book_id = int(row[0])
        rating = float(row[1])
        totalratings = int(row[2])
        cursor.execute('''
            UPDATE book
            SET rating = ?, totalratings = ?
            WHERE book.book_id = ?
        ''', (rating, totalratings, book_id))
    connection.commit()

print("#################################")
print("#       Processing genres       #")
print("#################################")
print()

cursor.execute('DROP TABLE IF EXISTS genre')
cursor.execute('''
    CREATE TABLE genre(
        genre_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        num_books INTEGER NOT NULL
    )
''')

cursor.execute('DROP TABLE IF EXISTS genre_book')
cursor.execute('''
    CREATE TABLE genre_book(
        genre_id INTEGER,
        book_id INTEGER,
        PRIMARY KEY (genre_id, book_id),
        FOREIGN KEY(book_id) REFERENCES book(book_id),
        FOREIGN KEY(genre_id) REFERENCES genre(genre_id)
    )

''')

with open('genres.csv') as genres_csv:
    csv_reader = csv.reader(genres_csv, delimiter=',')
    next(csv_reader, None)
    i = 0
    for row in csv_reader:
        print('Processing row {} of 1184'.format(i), end="\r")
        genre_id = i
        i += 1
        genre = row[0]
        num_books = int(row[1])
        ids = list(map(lambda x: int(x), row[2].split(',')))
        cursor.execute('''
            INSERT INTO genre(genre_id, name, num_books)
            VALUES (?,?,?)
        ''', (genre_id, genre, num_books))
        for id in ids:
            cursor.execute('''
                INSERT INTO genre_book(genre_id, book_id)
                VALUES (?,?)
            ''', (genre_id, id))


    connection.commit()


print("#################################")
print("#       Processing authors      #")
print("#################################")
print()


cursor.execute('DROP TABLE IF EXISTS author')
cursor.execute('''
    CREATE TABLE author(
        author_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        num_books INTEGER NOT NULL,
        average_rating REAL NOT NULL
    )
''')

cursor.execute('DROP TABLE IF EXISTS author_book')
cursor.execute('''
    CREATE TABLE author_book(
        author_id INTEGER,
        book_id INTEGER,
        PRIMARY KEY (author_id, book_id),
        FOREIGN KEY(book_id) REFERENCES book(book_id),
        FOREIGN KEY(author_id) REFERENCES author(author_id)
    )

''')

with open('authors.csv') as authors_csv:
    csv_reader = csv.reader(authors_csv, delimiter=',')
    next(csv_reader, None)
    i = 0
    for row in csv_reader:
        print('Processing row {} of 87306'.format(i), end="\r")
        author_id = i
        i += 1
        author = row[0]
        num_books = int(row[2])
        average_rating = float(row[3])
        ids = list(map(lambda x: int(x), row[1].split(',')))
        cursor.execute('''
            INSERT INTO author(author_id, name, num_books, average_rating)
            VALUES (?,?,?,?)
        ''', (author_id, author, num_books, average_rating))
        for id in ids:
            try:
                cursor.execute('''
                    INSERT INTO author_book(author_id, book_id)
                    VALUES (?,?)
                ''', (author_id, id))
            except:
                print()
                print(author_id)
                print(id)
                print(ids)
                raise Exception

    connection.commit()
