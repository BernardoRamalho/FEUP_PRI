import pandas as pd
import os
import sys

clean_df = pd.read_csv('dataset.csv')

if not os.path.exists('genres.csv'):

    print("# Generating file 'genres.csv'.")

    # Generate the genres dataset
    genres_df = clean_df[['book_id', 'genre']].copy()
    genres_dict = {}

    for index, row in genres_df.iterrows():
        genres = str(row['genre']).split(',')
        book_id = str(row['book_id'])
        for genre in genres:
            if genre not in genres_dict:
                genres_dict[genre] = [book_id]
            else:
                genres_dict[genre].append(book_id)
            
    genres_list = []
    num_books = []
    for genre_list in [*genres_dict.values()]:
        genres_list.append(','.join(genre_list))
        num_books.append(len(genre_list))

    final_genres_df = pd.DataFrame({
        'genre': [*genres_dict.keys()],
        'num_books': num_books,
        'ids': genres_list
        })

    print("## Sorting the dataframe.")
    final_genres_df = final_genres_df.sort_values(by=['genre'])

    print("# File 'genres.csv' generated successfully.")
    print()

    # Save the genres dataset
    final_genres_df.to_csv('genres.csv', index=False)
else:
    print("# File 'genres.csv' already exists, skipping generation for this file.")
    print()

if not os.path.exists('ratings.csv'):
    # Generate the ratings dataset
    print("# Generating file 'ratings.csv'.")

    ratings_df = clean_df[['book_id', 'rating', 'totalratings']].copy()

    ratings_df.to_csv('ratings.csv', index=False)

    print("# File 'ratings.csv' generated successfully.")
    print()
else:
    print("# File 'ratings.csv' already exists, skipping generation for this file.")
    print()

if not os.path.exists('authors.csv'):
    # Generate the authors dataset

    print("# Generating file 'authors.csv'.")
    
    authors_dict = {}

    authors_df = clean_df[['book_id', 'author']].copy()

    i = 0
    for index, row in authors_df.iterrows():
        authors = str(row['author']).split(',')
        book_id = str(row['book_id'])

        for author in authors:
            if author[0] == ' ':
                author = author[1:]
            if author not in authors_dict:
                authors_dict[author] = [book_id]
            else:
                authors_dict[author].append(book_id)

    authors_list = []
    n_books = []
    for author_list in [*authors_dict.values()]:
        authors_list.append(','.join(author_list))
        n_books.append(len(author_list))        

    intermediate_authors_df = pd.DataFrame({
        'author': [*authors_dict.keys()],
        'ids': authors_list,
        'num_books': n_books
        })

    print("## Calculating the average rating for each author.")

    averages = []

    for index, row in intermediate_authors_df.iterrows():
        ids = list(map(lambda x: int(x), str(row['ids']).split(',')))
        average = 0.0
        for id in ids:
            try:
                average += float(clean_df.iloc[id]['rating'])
            except:
                print(id)

        averages.append(average/len(ids))
    
    final_authors_df = pd.DataFrame({
        'author': [*authors_dict.keys()],
        'ids': authors_list,
        'num_books': n_books,
        'average_rating': averages
    })

    print("## Sorting the dataframe.")
    final_authors_df = final_authors_df.sort_values(by=['author'])

    final_authors_df.to_csv('authors.csv', index=False)

    print("# File 'authors.csv' generated successfully.")
    print()
else:
    print("# File 'authors.csv' already exists, skipping generation for this file.")
    print()

if not os.path.exists('books.csv'):
    # Generate the books dataset
    print("# Generating file 'books.csv'.")

    clean_df = clean_df.drop(['genre', 'author', 'rating', 'totalratings'], axis=1)

    clean_df.to_csv('books.csv', index=False)

    print("# File 'books.csv' generated successfully.")
    print()
else:
    print("# File 'books.csv' already exists, skipping generation for this file.")
    print()
