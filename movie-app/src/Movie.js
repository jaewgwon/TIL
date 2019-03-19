import React from 'react';
import PropTypes from 'prop-types';
import './Movie.css';


function Movie ({title, coverImage}) {
	return (
	<div>
		<BookCover coverImage={coverImage} />
		<h1>{title}</h1>
	</div>)
}

function BookCover({coverImage}) {

	return <img src={coverImage} />
}

Movie.propTypes = {
	title: PropTypes.string.isRequired,
	coverImage: PropTypes.string.isRequired
}

export default Movie;