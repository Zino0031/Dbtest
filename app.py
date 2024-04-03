from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = [
    {"id": 1, "name": "John Doe", "phone": "11111111111", "password": "pass1", "email": "john_doe@gmail.com"},
    {"id": 2, "name": "Jane Doe", "phone": "22222222222", "password": "pass2", "email": "jane_doe@gmail.com"},
    {"id": 3, "name": "Mark Doe", "phone": "3333333333", "password": "pass3", "email": "mark_doe@gmail.com"},
    {"id": 4, "name": "Macy Doe", "phone": "4444444444", "password": "pass4", "email": "macy_doe@gmail.com"}
]

movies = [
    {"id": 1, "name": "Home Alone", "genre": "Comedy", "rating": "PG", "release_date": "01-04-1996"},
    {"id": 2, "name": "The Godfather", "genre": "Crime", "rating": "R", "release_date": "01-04-1972"},
    {"id": 3, "name": "Avengers: Endgame", "genre": "Action", "rating": "PG", "release_date": "01-04-2019"}
]

ratings = [
    {"id": 1, "user_id": 1, "movie_id": 1, "rating": 5.0},
    {"id": 2, "user_id": 1, "movie_id": 2, "rating": 4.0},
    {"id": 3, "user_id": 1, "movie_id": 3, "rating": 3.3},
    {"id": 4, "user_id": 2, "movie_id": 1, "rating": 5.0},
    {"id": 5, "user_id": 2, "movie_id": 3, "rating": 4.5},
    {"id": 6, "user_id": 3, "movie_id": 1, "rating": 1.6},
    {"id": 7, "user_id": 3, "movie_id": 2, "rating": 0.0},
    {"id": 8, "user_id": 3, "movie_id": 3, "rating": 3.4},
    {"id": 9, "user_id": 4, "movie_id": 2, "rating": 4.5}
]

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = next((user for user in users if user['email'] == email and user['password'] == password), None)
    if user:
        return jsonify({"message": "Login successful", "user": user}), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({"movies": movies}), 200

@app.route('/add_movie', methods=['POST'])
def add_movie():
    data = request.get_json()
    movies.append(data)
    return jsonify({"message": "Movie added successfully"}), 201

@app.route('/rate_movie', methods=['POST'])
def rate_movie():
    data = request.get_json()
    user_id = data.get('user_id')
    movie_id = data.get('movie_id')
    rating = data.get('rating')
    rating_entry = {"id": len(ratings) + 1, "user_id": user_id, "movie_id": movie_id, "rating": rating}
    ratings.append(rating_entry)
    return jsonify({"message": "Rating added successfully"}), 201

@app.route('/movie/<int:movie_id>', methods=['GET'])
def get_movie_details(movie_id):
    movie = next((movie for movie in movies if movie['id'] == movie_id), None)
    if movie:
        movie_ratings = [rating['rating'] for rating in ratings if rating['movie_id'] == movie_id]
        average_rating = sum(movie_ratings) / len(movie_ratings) if movie_ratings else 0
        movie['average_rating'] = average_rating
        return jsonify({"movie": movie}), 200
    else:
        return jsonify({"message": "Movie not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
