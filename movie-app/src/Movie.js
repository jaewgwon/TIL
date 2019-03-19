import React, { Component } from 'react';
import PropTypes from 'prop-types';
import './Movie.css';


class Movie extends Component {

	static propTypes = {
		title: PropTypes.string.isRequired,
		coverImage: PropTypes.string
	}

	render() {
		return (
			<div>
				<BookCover coverImage={this.props.coverImage}/>
				<h1>{this.props.title}</h1>
			</div>
		);
	}
}

class BookCover extends Component {
	static porpTypes = {
		coverImage: PropTypes.string.isRequired
	}

	render() {
		return (
			<img src={this.props.coverImage}/>
		);
	}
}

export default Movie;
