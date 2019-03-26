import React, { Component } from 'react';
import './App.css';
import Movie from './Movie';


class App extends Component {
  state = {}
  
  componentDidMount() {
    this._getMovies();
  }
  
  _getMovies = async () => {
    // whatever the result is, put it into movies
    const movies = await this._callApi();
    this.setState({
      movies
    })
  }

  _callApi = () => {
     return fetch('https://yts.am/api/v2/list_movies.json?sort_by=rating')
    .then(response => response.json())
    .then(result => result.data.movies)
    .catch(err => console.log(err))
  }

  _renderMovies = () => {
    const movies = this.state.movies.map((movie) => 
      <Movie title={movie.title} large_cover_image={movie.large_cover_image} key={movie.id} />
    )
    return movies
  }

  render() {
    return (
      <div className="App">
        {this.state.movies ? this._renderMovies() : 'Loading'}
      </div>
    );
  }
}

export default App;