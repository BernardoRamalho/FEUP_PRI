
import sys
import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np

filenames = ["query1_rel.txt", "query2_rel.txt", "query3_rel.txt"]
query_urls = [
    "http://localhost:8983/solr/books/select?q=fiction%20paperback&q.op=OR&defType=edismax&indent=true&rows=100&qf=author%5E1%20desc%5E1%20title%5E1%20genre%5E1%20bookformat%5E1",
    "http://localhost:8983/solr/books/select?q=histor*%20religio*&q.op=OR&defType=edismax&indent=true&rows=100&qf=author%5E1%20desc%5E1%20title%5E1%20genre%5E1%20bookformat%5E1",
    "http://localhost:8983/solr/books/select?q=paul%20war&q.op=OR&defType=edismax&indent=true&rows=100&qf=author%5E1%20desc%5E1%20title%5E1%20genre%5E1%20bookformat%5E1"
]

query_url = ""
rel_filename = ""

if len(sys.argv) < 2:
    print("Please specify which query you want to evaluate")
else:
    if 3 < int(sys.argv[1]) < 1:
        print("Invalid query, needs to be between 1 and 3")
        sys.exit()
    rel_filename = filenames[int(sys.argv[1]) - 1]
    query_url = query_urls[int(sys.argv[1]) - 1]

relevant = list(map(lambda el: int(el.strip()), open(rel_filename, 'r').readlines()))

results = requests.get(query_url).json()['response']['docs']

print(results[0]['book_id'][0])

# METRICS TABLE
# Define custom decorator to automatically calculate metric based on key
metrics = {}
metric = lambda f: metrics.setdefault(f.__name__, f)

@metric
def ap(results, relevant):
    """Average Precision"""
    precision_values = [
        len([
            doc 
            for doc in results[:idx]
            if doc['book_id'][0] in relevant
        ]) / idx 
        for idx in range(1, len(results))
    ]
    return sum(precision_values)/len(precision_values)

@metric
def p10(results, relevant, n=10):
    """Precision at N"""
    return len([doc for doc in results[:n] if doc['book_id'][0] in relevant])/n

def calculate_metric(key, results, relevant):
    return metrics[key](results, relevant)

# Define metrics to be calculated
evaluation_metrics = {
    'ap': 'Average Precision',
    'p10': 'Precision at 10 (P@10)'
}

# Calculate all metrics and export results as LaTeX table
df = pd.DataFrame([['Metric','Value']] +
    [
        [evaluation_metrics[m], calculate_metric(m, results, relevant)]
        for m in evaluation_metrics
    ]
)

with open('results.tex','w') as tf:
    tf.write(df.to_latex())

# PRECISION-RECALL CURVE
# Calculate precision and recall values as we move down the ranked list
precision_values = [
    len([
        doc 
        for doc in results[:idx]
        if doc['book_id'][0] in relevant
    ]) / idx 
    for idx, _ in enumerate(results, start=1)
]

recall_values = [
    len([
        doc for doc in results[:idx]
        if doc['book_id'][0] in relevant
    ]) / len(relevant)
    for idx, _ in enumerate(results, start=1)
]

precision_recall_match = {k: v for k,v in zip(recall_values, precision_values)}

# Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
recall_values = sorted(set(recall_values))

# Extend matching dict to include these new intermediate steps
for idx, step in enumerate(recall_values):
    if step not in precision_recall_match:
        if recall_values[idx-1] in precision_recall_match:
            precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
        else:
            precision_recall_match[step] = precision_recall_match[recall_values[idx+1]]

disp = PrecisionRecallDisplay([precision_recall_match.get(r) for r in recall_values], recall_values)
disp.plot()
plt.savefig('precision_recall1.pdf')
