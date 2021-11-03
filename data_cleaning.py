
import pandas as pd

df = pd.read_csv('GoodReads_100k_books.csv')

# Drop the isbn13 column, as it is not useful
df = df.drop(['isbn13'], axis=1)

# Drop the row corresponding to a book that has no title
df = df.drop(df[df['title'].isnull()].index)

# Replace missing values
df['bookformat'] = df['bookformat'].fillna("Unknown")
df['desc'] = df['desc'].fillna("No description available")
df['genre'] = df['genre'].fillna("Unknown")
df['img'] = df['img'].fillna("Not available")
df['isbn'] = df['isbn'].fillna("Not available")

df.index.name = 'book_id'

# Save the cleaned dataset on a new csv file
df.to_csv('dataset.csv')