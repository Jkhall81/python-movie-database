import storage_json
import movie_app

storage = storage_json.StorageJson('data.json')
movie_app = movie_app.MovieApp(storage)


def main():
    movie_app.user_interaction()


if __name__ == '__main__':
    main()
