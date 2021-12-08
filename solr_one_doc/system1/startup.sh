#!/bin/bash

precreate-core books

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 10

# Populate collection
bin/post -c books /data/data.json

# Restart in foreground mode so we can access the interface
solr restart -f
