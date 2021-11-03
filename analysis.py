
# Colunas numéricas sem valores nulos
# Coluna author, link sem valores nulos

# bookformat, desc, genre, img, isbn e isbn13 com valores nulos
# Coluna title com um valor nulo

import pandas as pd

data = pd.read_csv("GoodReads_100k_books.csv")

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