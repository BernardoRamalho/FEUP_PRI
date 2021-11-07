
# Colunas numéricas sem valores nulos
# Coluna author, link sem valores nulos

# bookformat, desc, genre, img, isbn e isbn13 com valores nulos
# Coluna title com um valor nulo

import pandas as pd


data = pd.read_csv("GoodReads_100k_books.csv")
genres = pd.read_csv("genres.csv") #make sure it's this name
authors = pd.read_csv("authors.csv") #make sure it's this name
books = pd.read_csv("books.csv") #make sure it's this name
ratings = pd.read_csv("ratings.csv") #make sure it's this name

'''
data.bookformat = data.bookformat.fillna("Not specified")
data.desc = data.desc.fillna("No description available")
data.genre = data.genre.fillna("None")
data.img = data.img.fillna("No image available")
data.isbn = data.isbn.fillna("Not available")
data.isbn13 = data.isbn13.fillna("Not available")
'''

#print(data[data["pages"] == 0].sum())
#print(data.nunique())
print(data.info())

#print(data.title.isna().sum())

#data = data.fillna("None")

#print(data.loc[[30]])


# __________________________________________________________________________________
# Data Characterization Tutorial

# Mean

# Median 

# Describe

# Data Visualiation

## use plots 
### kinds: bar, histogram, density, box

# Calculate

## Average rating per author
## Book formats percentages
## Most read genres
## Books and genres with the best rating
## Top 0.1% of books


