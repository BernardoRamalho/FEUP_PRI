import pandas as pd
import os

clean_df = pd.read_csv('dataset.csv')

if not os.path.exists('genres.csv'):

    # Generate the genres dataset
    genres_df = clean_df[['book_id', 'genre']].copy()
    ids_list = []
    genres_list = []
    genres_dict = {}

    for index, row in genres_df.iterrows():
        genres = str(row['genre']).split(',')
        book_id = int(row['book_id'])
        for genre in genres:
            '''
            if genre not in genres_dict:
                genres_dict[genre] = [book_id]
            else:
                genres_dict[genre].append(book_id)
            '''
            ids_list.append(book_id)
            genres_list.append(genre)

    assert(len(ids_list) == len(genres_list))

    final_genres_df = pd.DataFrame({
        'book_id': ids_list,
        'genre': genres_list
        })

    '''
    assert(len(genres_dict.keys()) == len(genres_dict.values()))

    alt_genres_df = pd.DataFrame({
        'genre': genres_dict.keys(),
        'ids': genres_dict.values()
    })
    '''

    # Save the genres dataset
    final_genres_df.to_csv('genres.csv', index=False)
    #alt_genres_df.to_csv('alt_genres.csv', index=False)

if not os.path.exists('ratings.csv'):

    # Generate the ratings dataset
    ratings_df = clean_df[['book_id', 'rating', 'totalratings']].copy()

    ratings_df.to_csv('ratings.csv', index=False)

if not os.path.exists('authors.csv'):

    # Generate the authors dataset

    # Not implemented yet
    pass