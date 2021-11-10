
# Makefile

# Run 'make' to execute pipeline
# Run 'make clean' to delete data files

###############
#    Rules    #
###############

all: dataset.csv authors.csv books.csv genres.csv ratings.csv books.db

# Rule to clean the original dataset
# Data cleaning steps:
# 	- Drop columns that are not useful
# 	- Drop rows with missing critical data (only one row is dropped because it has no book title)
# 	- Replace missing values on non-critical columns with placeholders such as 'Unknown' or 'Not available'
# 	- Remove duplicate author names and genres
# 	- Trim the author names (some had leading or trailing whitespaces)
# 	- Add an id column to the dataset
dataset.csv: GoodReads_100k_books.csv
	python data_cleaning.py
	echo "Data cleaning finished, dataset.csv is ready"

# Rule to split the clean dataset into four smaller datasets to make the data exploration process easier
# Performs some calculations and adds the results as new columns aswell
# The datasets:
# 	- authors.csv: has the number of books each author has written (new column) and the id of each of those books
# 	- genres.csv: has the number of books of each genre (new column) and the id of each of those books
# 	- ratings.csv: has the rating information for each book on the dataset (the book's average rating and the total number of ratings it has)
# 	- books.csv: has the remaining information about the books (isbn, image. link, etc.)
authors.csv books.csv genres.csv ratings.csv: dataset.csv
	python split_dataset.py
	echo "Dataset splitting finished, authors.csv, books.csv, genres.csv and ratings.csv are ready"

# Rule to create an SQL database with the information of the csv's. 
# We create a table for authors, books and genres.
# We also create two tables to represent the realtion between authors<-->books and genres<-->books (they only have two columns representing the id of each object).
# The tables have the sabe columns as the corresponding csv except the books' table which we added the ratings information to it. 
books.db: authors.csv books.csv genres.csv ratings.csv
	python to_sqlite.py 
	echo "Database created successfully, books.db is ready"

# Deletes all the files created with this make file
clean:
	rm -f dataset.csv authors.csv books.csv genres.csv ratings.csv books.db