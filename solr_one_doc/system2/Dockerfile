FROM solr:8.10

# Json datasets

COPY dataset.json /data/data.json

# Schemas

COPY data_schema.json /data/data_schema.json

# Stopwords file

COPY stopwords.txt /data/stopwords.txt

# Startup Script

COPY startup.sh /scripts/startup.sh

CMD chmod +x /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]

