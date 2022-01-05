import React from 'react'
import ReactDOM from 'react-dom'
import SolrConnector from 'react-solr-connector';

// import express from "express";
// import pkg from "body-parser";


// const { json, urlencoded } = pkg;

// const app = express();
// const PORT = process.env.port || 8080;

// app.use(json());
// app.use(function (req, res, next) {
//   res.header("Access-Control-Allow-Origin", "http://localhost:8983");
//   res.header("Access-Control-Allow-Headers", "*");
//   next();
// });
// app.use(urlencoded({ extended: true }));

// app.post("/startSimulation", (req, res) => {
// });

// app.listen(PORT, () =>
//   console.log(`Server listening at http://localhost:${PORT}`)
// );

{/* <SolrConnector searchParams={searchParams}>
  <SearchApp/>
</SolrConnector> */}

class SearchApp extends React.Component {


    render() {

        fetch('http://localhost:8983/solr/books/select?q=fiction%20paperback&q.op=OR&defType=edismax&indent=true&rows=100&qf=author%5E1%20desc%5E1%20title%5E1%20genre%5E1%20bookformat%5E1')
        .then(response => console.log(response.json()))
        return(<div>
            "adfasdf"

        </div>)
    }
  }
  

{/* <SolrConnector searchParams={searchParams}>
  <SearchApp/>
</SolrConnector> */}



// ========================================

ReactDOM.render(
    <SearchApp />,
    document.getElementById('root')
  );
  