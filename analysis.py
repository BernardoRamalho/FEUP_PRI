
# Colunas numéricas sem valores nulos
# Coluna author, link sem valores nulos

# bookformat, desc, genre, img, isbn e isbn13 com valores nulos
# Coluna title com um valor nulo

import pandas as pd
import matplotlib.pyplot as plt

genres = pd.read_csv("genres.csv") #make sure it's this name
authors = pd.read_csv("authors.csv") #make sure it's this name
books = pd.read_csv("books.csv") #make sure it's this name
ratings = pd.read_csv("ratings.csv") #make sure it's this name

# Distribution of book ratings
ratings_list = [0, 0, 0, 0, 0, 0]

for index, row in ratings.iterrows():
    ratings_list[int(row['rating'])] += 1

ratings_list
    
plt.bar([0, 1, 2, 3, 4, 5], ratings_list, color='green')
plt.show()

# Bookformats
chart_data = [0, 0, 0, 0]
translation = ['Hardcover', 'Paperback', 'Other', 'Unknown']
for index, row in books.iterrows():
    bookformat = row['bookformat']
    if bookformat == 'Hardcover':
        chart_data[0] += 1
    elif bookformat == 'Paperback':
        chart_data[1] += 1
    elif bookformat == 'Unknown':
        chart_data[3] += 1
    else:
        chart_data[2] += 1

fig1, chart = plt.subplots()
chart.pie(chart_data,labels=translation, shadow=True, autopct='%1.1f%%', startangle=90)
chart.axis('equal')
plt.tight_layout()

# Book Characterization
num_formats = books['bookformat'].nunique()
average_pages = books['pages'].mean()
average_num_reviews = books['reviews'].mean()
total_reviews = books['reviews'].sum()

plt.bar(['Number of formats', 'Average number of pages', 'Average number of reviews'], [num_formats, average_pages, average_num_reviews], color='red')
plt.tight_layout()

# Average rating authors
ratings_list = [0, 0, 0, 0, 0, 0]

for index, row in authors.iterrows():
    ratings_list[int(row['average_rating'])] += 1

ratings_list
    
plt.bar([0, 1, 2, 3, 4, 5], ratings_list, color='green')
plt.show()

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


