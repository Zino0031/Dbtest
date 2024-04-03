import React, { useState, FormEvent } from 'react';

const MovieForm: React.FC = () => {
  const [name, setName] = useState('');
  const [genre, setGenre] = useState('');
  const [rating, setRating] = useState('');
  const [releaseDate, setReleaseDate] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/add_movie', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, genre, rating, release_date: releaseDate }),
      });

      if (response.ok) {
        setMessage('Movie added successfully');
        setName('');
        setGenre('');
        setRating('');
        setReleaseDate('');
        
      } else {
        const data = await response.json();
        setMessage(data.message);
      }
    } catch (error) {
      console.error('Error:', error);
      setMessage('An error occurred. Please try again later.');
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-4">
      <h2 className="text-xl font-semibold mb-4">Add Movie</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label htmlFor="name" className="block text-sm font-medium text-gray-700">Name:</label>
          <input type="text" id="name" value={name} onChange={(e) => setName(e.target.value)} className="mt-1 p-2 border border-gray-300 rounded-md w-full" required />
        </div>
        <div className="mb-4">
          <label htmlFor="genre" className="block text-sm font-medium text-gray-700">Genre:</label>
          <input type="text" id="genre" value={genre} onChange={(e) => setGenre(e.target.value)} className="mt-1 p-2 border border-gray-300 rounded-md w-full" required />
        </div>
        <div className="mb-4">
          <label htmlFor="rating" className="block text-sm font-medium text-gray-700">Rating:</label>
          <input type="text" id="rating" value={rating} onChange={(e) => setRating(e.target.value)} className="mt-1 p-2 border border-gray-300 rounded-md w-full" required />
        </div>
        <div className="mb-4">
          <label htmlFor="releaseDate" className="block text-sm font-medium text-gray-700">Release Date:</label>
          <input type="text" id="releaseDate" value={releaseDate} onChange={(e) => setReleaseDate(e.target.value)} className="mt-1 p-2 border border-gray-300 rounded-md w-full" required />
        </div>
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:bg-blue-600">Add Movie</button>
      </form>
      {message && <p className="text-sm mt-2 text-green-500">{message}</p>}
    </div>
  );
};

export default MovieForm;
