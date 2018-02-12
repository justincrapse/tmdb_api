import requests

from tmdb_test_context import TMDBTestContext


class TMDBTestCase:
    """ This class contains common functions to be shared by many test cases """
    @staticmethod
    def search_for_movie_by_title_and_release_date(tc: TMDBTestContext, movie):
        request_title = movie['title'].replace(' ', '+')
        request_string = tc.base_url + f'/search/movie?api_key={tc.api_key}&query={request_title}'
        results = requests.get(url=request_string).json()
        for result in results['results']:
            if result['release_date'] == movie['info']['release_date']:
                return result
        return None

    @staticmethod
    def get_movie_id(tc, movie):
        movie_dict = TMDBTestCase.search_for_movie_by_title_and_release_date(tc=tc, movie=movie)
        return movie_dict['id']
