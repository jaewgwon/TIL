import React, { Component } from 'react';
import './App.css';
import Movie from './Movie';

const books = [
  {
    title : "철학은 어떻게 삶의 무기가 되는가",
    coverImage : "https://bookthumb-phinf.pstatic.net/cover/144/574/14457455.jpg?udate=20190313"
  },
  {
    title : "공부머리 독서법",
    coverImage : "https://bookthumb-phinf.pstatic.net/cover/135/131/13513128.jpg?udate=20190214"
  },
  {
    title : "고요할수록 밝아지는 것들",
    coverImage : "https://bookthumb-phinf.pstatic.net/cover/142/545/14254551.jpg?type=m140&udate=20190220"
  },
  {
    title : "에어프라이어 만능 레시피북",
    coverImage : "https://bookthumb-phinf.pstatic.net/cover/144/808/14480846.jpg?udate=20190312"
  }
]

class App extends Component {
  state = {
    greetings: "Hello!"
  }
  
  componentDidMount() {
    setTimeout(() => {
      this.setState({
        greetings: "Hello again!"
      })
    }, 2000)
  }

  render() {
    return (
      <div className="App">
        {this.state.greetings}
        {books.map((book, index) => 
          <Movie title={book.title} coverImage={book.coverImage} key={index} />
        )}
      </div>
    );
  }
}

export default App;
