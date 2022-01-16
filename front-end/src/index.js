import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios';



class SearchApp extends React.Component {

    constructor(props){
      super(props);
      this.data = null;
      
    }

    getQuery(){
      console.log("QUERYRYRYRYRYYRYR")
      axios('http://localhost:8983/solr/books/select?q=fiction%20paperback&q.op=OR&defType=edismax&indent=true&rows=100&qf=author%5E1%20desc%5E1%20title%5E1%20genre%5E1%20bookformat%5E1')
      .then( response => {this.setData(response.data)})
    }

    setData(data){
      console.log(data)
      this.data = data
      console.log(this.data)
    }

    render() {
        this.getQuery();
        

        console.log(this.data)

        return(<div>

            <div>
              {this.data.docs[0]}
            </div>
            

        </div>
        )
    }
  }
  
ReactDOM.render(
    <SearchApp />,
    document.getElementById('root')
  );
  