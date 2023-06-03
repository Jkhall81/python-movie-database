import argparse
import storage_json
import storage_csv
import movie_app

parser = argparse.ArgumentParser(description='Movie App')

parser.add_argument('file', help='Path to the data file (JSON or CSV)')

args = parser.parse_args()
file_path = args.file

if file_path.endswith('.json'):
    storage = storage_json.StorageJson(file_path)
    movie_app = movie_app.MovieApp(storage)
elif file_path.endswith('.csv'):
    storage = storage_csv.StorageCsv(file_path)
    movie_app = movie_app.MovieApp(storage)


def main():
    movie_app.user_interaction()


if __name__ == '__main__':
    main()
