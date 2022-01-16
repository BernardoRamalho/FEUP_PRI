
from flask import Flask, render_template, request, redirect, url_for, session
import requests
import os
import math

app = Flask(__name__)

def build_url(search_str, fields, reviews, rating_range, pages_range, reviews_range, totalratings_range, sort_params):
    
    reviews_search_str = ""
    normal_search_str = ""
    if reviews:
        reviews_search_str = f'{{!parent which="type:book" score=max}}{{!edismax qf="review^4" v="{search_str}"}}'
    if len(fields) != 0:
        normal_search_str = f'{{!edismax qf="{fields}" v="{search_str}"}}'

    q = "*:*"
    if reviews_search_str != "":
        q = " " + reviews_search_str
        if normal_search_str != "":
            q += " OR " + normal_search_str
    elif normal_search_str != "":
        q = " " + normal_search_str

    fq_rating = f"rating:[{rating_range[0]} TO {rating_range[1]}]"
    fq_pages = f"pages:[{pages_range[0]} TO {pages_range[1]}]"
    fq_reviews = f"num_reviews:[{reviews_range[0]} TO {reviews_range[1]}]"
    fq_totalratings = f"totalratings:[{totalratings_range[0]} TO {totalratings_range[1]}]"

    sort_str = f"{sort_params[0]} {sort_params[1]}"

    fq = "type:book"
    url = f"http://localhost:8983/solr/books/select?q={q}&fl=*,score,[child]&fq={fq}&fq={fq_rating}&fq={fq_pages}&fq={fq_reviews}&fq={fq_totalratings}&q.op=OR&defType=lucene&indent=true&sort={sort_str}&rows=10"

    return url

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/results")
def results():

    page = request.args.get('page')
    print("Page:", page)

    query_url = session['query_url']
    query_url = query_url +  f"&start={(int(page) - 1) * 10}"
    print(query_url)
    response = requests.get(query_url).json()['response']
    results = response['docs']
    num_docs = response['numFound']

    num_pages = math.ceil(num_docs / 10.0)

    return render_template('results.html', results=results, page=page, num_pages=num_pages)

@app.route("/search", methods=['POST'])
def search():
    search_str = request.form['search_str']
    search_fields = ""
    fields = ['title', 'desc', 'author', 'genre', 'bookformat']
    weights = ['^0.5', '^0.2', '^1.2', '^1.3', '^1.3']
    for i, field in enumerate(fields):
        if field + 'Field' in request.form:
            search_fields += field + weights[i] + ' '
    reviews = False
    if 'reviewsField' in request.form:
        reviews = True
    page = request.form['page']
    ratingStart = request.form['ratingStart']
    ratingEnd = request.form['ratingEnd']

    pagesStart = request.form['pagesStart']
    pagesEnd = request.form['pagesEnd']

    reviewsStart = request.form['reviewsStart']
    reviewsEnd = request.form['reviewsEnd']

    totalratingsStart = request.form['totalratingsStart']
    totalratingsEnd = request.form['totalratingsEnd']

    sort_field = request.form['sortField']
    sort_order = request.form['sortOrder']

    print(search_fields)

    query_url = build_url(search_str, search_fields, reviews, (float(ratingStart), float(ratingEnd)), (int(pagesStart), int(pagesEnd)), (int(reviewsStart), int(reviewsEnd)), (int(totalratingsStart), int(totalratingsEnd)), (sort_field, sort_order))

    print(query_url)
    session['query_url'] = query_url
    return redirect(url_for('results', page=page))

"""
@app.route("/showResults")
def home():
    query_url = "http://localhost:8983/solr/books/select?q=*:*&fq=!type:review&q.op=OR&defType=lucene&indent=true&rows=10"
    results = requests.get(query_url).json()['response']['docs']
    print(results)
    return render_template('results.html', results=results)
"""

app.secret_key = os.urandom(24)
app.run(debug = True)