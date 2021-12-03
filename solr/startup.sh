#!/bin/bash

precreate-core genres
precreate-core genre_books
precreate-core authors
precreate-core books
precreate-core author_books

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 10

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/author_book_schema.json \
    http://localhost:8983/solr/author_books/schema

sleep 1

curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/author_schema.json \
    http://localhost:8983/solr/authors/schema

sleep 1

curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/book_schema.json \
    http://localhost:8983/solr/books/schema

sleep 1

curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/genre_book_schema.json \
    http://localhost:8983/solr/genre_books/schema

sleep 1

curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/genre_schema.json \
    http://localhost:8983/solr/genres/schema

sleep 1

# Populate collection
bin/post -c genre_books /data/genre_book.json
bin/post -c genres /data/genre.json
bin/post -c authors /data/author.json
bin/post -c books /data/book.json
bin/post -c author_books /data/author_book.json

# Restart in foreground mode so we can access the interface
solr restart -f
