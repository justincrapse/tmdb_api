import pytest

from tmdb_test_context import TMDBTestContext

API_KEY = 'ef05a3d0bac674753a9809982fe155b8'
BASE_URL = 'https://api.themoviedb.org/3'


@pytest.fixture
def tc():
    test_context = TMDBTestContext(api_key=API_KEY, base_url=BASE_URL)
    return test_context
