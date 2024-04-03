import React from 'react';

interface Movie {
  id: number;
  name: string;
  genre: string;
  release_date: string;
}

interface Props {
  movies: Movie[];
}

const MovieList: React.FC<Props> = ({ movies }) => {
  return (
    <div className="grid grid-cols-3 gap-4">
      {movies?.map((movie, index) => (
        <div key={index} className="bg-white rounded-lg shadow-md p-4">
          <h3 className="text-lg font-semibold">{movie.name}</h3>
          <p className="text-sm text-gray-500">{movie.genre}</p>
          <p className="text-sm text-gray-500">{movie.release_date}</p>
        </div>
      ))}
    </div>
  );
};

export default MovieList;
