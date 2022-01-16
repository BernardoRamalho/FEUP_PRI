
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    query_url = "http://localhost:8983/solr/books/select?q=*:*&fq=!type:review&q.op=OR&defType=lucene&indent=true&rows=10"
    results = requests.get(query_url).json()['response']['docs']
    print(results)
    return render_template('index.html', results=results)

"""
@app.route("/showResults")
def home():
    query_url = "http://localhost:8983/solr/books/select?q=*:*&fq=!type:review&q.op=OR&defType=lucene&indent=true&rows=10"
    results = requests.get(query_url).json()['response']['docs']
    print(results)
    return render_template('results.html', results=results)
"""

app.run(debug = True)