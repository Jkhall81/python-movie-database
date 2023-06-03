import storage_json
import movie_app

test = storage_json.StorageJson('data.json')
movie1 = movie_app.MovieApp(test)

movie1._generate_website()
