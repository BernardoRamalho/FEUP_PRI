FROM solr:8.10

# Json datasets

COPY dataset.json /data/data.json

# Schemaless system

# Startup Script

COPY startup.sh /scripts/startup.sh

CMD chmod +x /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]

