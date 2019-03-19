import React, { Component } from 'react';
import './App.css';
import Movie from './Movie';


class App extends Component {
  state = {}
  
  componentDidMount() {
    fetch('https://yts.am/api/v2/list_movies.json?sort_by=rating')
    .then(response => response.json())
    .then(result => console.log(result))
    .catch(err => console.log(err))
  }

  _renderMovies = () => {
    const books = this.state.books.map((book, index) => 
      <Movie title={book.title} coverImage={book.coverImage} key={index} />
    )
    return books
  }

  render() {
    return (
      <div className="App">
        {this.state.books ? this._renderMovies() : 'Loading'}
      </div>
    );
  }
}

export default App;