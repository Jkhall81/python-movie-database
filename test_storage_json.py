import os
import pytest
from storage_json import StorageJson


def test_add_movie():
    file_path = 'test_movies.json'

    # Create the file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('{}')

    storage = StorageJson(file_path)
    storage.add_movie('Title 1', 2021, 7.5, 'https://example.com/poster1.jpg', 'Plot 1')
    movies = storage.list_movies()
    assert 'Title 1' in movies
    assert movies['Title 1']['rating'] == 7.5


def test_delete_movie():
    file_path = 'test_movies.json'
    storage = StorageJson(file_path)
    storage.add_movie('Title 1', 2021, 7.5, 'https://example.com/poster1.jpg', 'Plot 1')
    storage.delete_movie('Title 1')
    movies = storage.list_movies()
    assert len(movies) == 0


def test_update_movie():
    file_path = 'test_movies.json'
    storage = StorageJson(file_path)
    storage.add_movie('Title 1', 2021, 7.5, 'https://example.com/poster1.jpg', 'Plot 1')
    storage.update_movie('Title 1', rating=8.0)
    movies = storage.list_movies()
    assert movies['Title 1']['rating'] == 8.0


def test_return_ratings():
    file_path = 'test_movies.json'
    storage = StorageJson(file_path)
    storage.add_movie('Title 1', 2021, 7.5, 'https://example.com/poster1.jpg', 'Plot 1')
    storage.add_movie('Title 2', 2022, 8.3, 'https://example.com/poster2.jpg', 'Plot 2')
    storage.add_movie('Title 3', 2023, 6.8, 'https://example.com/poster3.jpg', 'Plot 3')
    ratings = storage.return_ratings()
    assert ratings == [7.5, 8.3, 6.8]
    os.remove(file_path)


pytest.main()
