FROM solr:8.10

# Json datasets

COPY book.json /data/book.json

COPY author.json /data/author.json

COPY genre.json /data/genre.json

COPY author_book.json /data/author_book.json

COPY genre_book.json /data/genre_book.json

# Schemas

COPY author_book_schema.json /data/author_book_schema.json

COPY author_schema.json /data/author_schema.json

COPY book_schema.json /data/book_schema.json

COPY genre_book_schema.json /data/genre_book_schema.json

COPY genre_schema.json /data/genre_schema.json

# Startup Script

COPY startup.sh /scripts/startup.sh

CMD chmod +x /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]

