import React from 'react';
import PropTypes from 'prop-types';
import './Movie.css';


function Movie ({title, large_cover_image}) {
	return (
	<div>
		<BookCover large_cover_image={large_cover_image} />
		<h1>{title}</h1>
	</div>)
}

function BookCover({large_cover_image}) {

	return <img src={large_cover_image} />
}

Movie.propTypes = {
	title: PropTypes.string.isRequired,
	large_cover_image: PropTypes.string.isRequired
}

export default Movie;