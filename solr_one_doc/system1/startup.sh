#!/bin/bash

precreate-core books

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 10

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/data_schema.json \
    http://localhost:8983/solr/books/schema

sleep 1

# Populate collection
bin/post -c books /data/data.json

# Restart in foreground mode so we can access the interface
solr restart -f
