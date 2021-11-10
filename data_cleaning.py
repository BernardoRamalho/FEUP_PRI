
import pandas as pd

df = pd.read_csv('GoodReads_100k_books.csv')

# Drop the isbn13 column, as it is not useful
df = df.drop(['isbn13'], axis=1)
print("# Column 'isbn13' dropped.")
print()

# Drop the row corresponding to a book that has no title
df = df.drop(df[df['title'].isnull()].index)
print("# Dropped rows that have no title.")
print()

# Replace missing values
df['bookformat'] = df['bookformat'].fillna("Unknown")
df['desc'] = df['desc'].fillna("No description available")
df['genre'] = df['genre'].fillna("Unknown")
df['img'] = df['img'].fillna("Not available")
df['isbn'] = df['isbn'].fillna("Not available")
print("# Replaced the missing values on columns 'bookformat', 'desc', 'genre', 'img' and 'isbn'.")
print()

# Remove duplicate genres and authors
for index, row in df.iterrows():
    genres = str(row['genre']).split(',')
    authors = str(row['author']).split(',')

    # Trim author names
    for i, author in enumerate(authors):
        authors[i] = authors[i].strip()

    no_dups_genres = list(set(genres))
    no_dups_authors = list(set(authors))

    df.at[index, 'genre'] = ','.join(no_dups_genres)
    df.at[index, 'author'] = ','.join(no_dups_authors)

print("# Removed duplicate genres and authors.")
print()

# Give the dataset an index that will also serve as each book's id
df = df.reset_index()
df = df.drop('index', axis=1)
df.index.name = 'book_id'
print("# Added the 'book_id' column.")
print()

# Save the cleaned dataset on a new csv file
df.to_csv('dataset.csv')
print("# Saved the dataset as 'dataset.csv'.")
