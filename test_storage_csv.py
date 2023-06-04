import os
import pytest
from storage_csv import StorageCsv


def test_add_movie():
    file_path = 'test_movies.csv'
    storage = StorageCsv(file_path)
    storage.add_movie('Title 1', 2021, 7.5, 'https://example.com/poster1.jpg', 'Plot 1')
    movies = storage.list_movies()
    assert 'Title 1' in movies
    assert movies['Title 1']['rating'] == 7.5
    os.remove(file_path)


def test_delete_movie():
    file_path = 'test_movies.csv'
    storage = StorageCsv(file_path)
    storage.add_movie('Title 1', 2021, 7.5, 'https://example.com/poster1.jpg', 'Plot 1')
    storage.delete_movie('Title 1')
    movies = storage.list_movies()
    assert len(movies) == 0
    os.remove(file_path)


def test_update_movie():
    file_path = 'test_movies.csv'
    storage = StorageCsv(file_path)
    storage.add_movie('Title 1', 2021, 7.5, 'https://example.com/poster1.jpg', 'Plot 1')
    storage.update_movie('Title 1', rating=8.0)
    movies = storage.list_movies()
    assert movies['Title 1']['rating'] == 8.0
    os.remove(file_path)


def test_return_ratings():
    file_path = 'test_movies.csv'
    storage = StorageCsv(file_path)
    storage.add_movie('Title 1', 2021, 7.5, 'https://example.com/poster1.jpg', 'Plot 1')
    storage.add_movie('Title 2', 2022, 8.0, 'https://example.com/poster2.jpg', 'Plot 2')
    storage.add_movie('Title 3', 2023, 6.5, 'https://example.com/poster3.jpg', 'Plot 3')
    ratings = storage.return_ratings()
    assert ratings == [7.5, 8.0, 6.5]
    os.remove(file_path)


pytest.main()
