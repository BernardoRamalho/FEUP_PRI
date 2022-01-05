import React from 'react'
import ReactDOM from 'react-dom'


class SearchApp extends React.Component {


    render() {

        fetch('http://localhost:8983/solr/books/select?q=fiction%20paperback&q.op=OR&defType=edismax&indent=true&rows=100&qf=author%5E1%20desc%5E1%20title%5E1%20genre%5E1%20bookformat%5E1')
        .then(response => console.log(response.json()))
        return(<div>
            "adfasdf"

        </div>)
    }
  }
  

// ========================================

ReactDOM.render(
    <SearchApp />,
    document.getElementById('root')
  );
  