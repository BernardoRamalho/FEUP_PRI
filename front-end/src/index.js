import React from 'react'
import ReactDOM from 'react-dom'


class SearchApp extends React.Component {

    render() {

        let user_query = "job";
        let search_fields = encodeURIComponent("author desc title genre bookformat review")

        fetch(`http://localhost:8983/solr/books/select?q=${user_query}%20OR%20%7B!parent%20which%3D%22type:book%22%7D%7B!edismax%20qf%3D%22review%22%20v%3D%22${user_query}%22%7D&q.op=OR&defType=edismax&indent=true&qf=${search_fields}&fl=*,%20%5Bchild%5D&fq=!type:review&rows=100`)
        .then(response => response.text())
        .then((response) => console.log(JSON.parse(response)['response']['docs']))
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
  