from time import sleep

import pytest
import requests

from movie_data import movie_titles
from tmdb_test_case import TMDBTestCase
from tmdb_test_context import TMDBTestContext


class TestTMDB(TMDBTestCase):
    @pytest.mark.regression
    @pytest.mark.completed
    def test_get_movie_credits(self, tc: TMDBTestContext):
        random_movie = movie_titles.random_movie()
        movie_id = self.get_movie_id(tc=tc, movie=random_movie)
        request_string = f'/movie/{movie_id}/credits?api_key={tc.api_key}'
        credits_result = requests.get(tc.base_url + request_string)
        assert credits_result.status_code == 200

    @pytest.mark.regression
    @pytest.mark.completed
    def test_guest_movie_rating(self, tc: TMDBTestContext):
        random_movie = movie_titles.random_movie()
        movie_id = self.get_movie_id(tc=tc, movie=random_movie)
        request_string = tc.base_url + \
                         f'/movie/{movie_id}/rating?api_key={tc.api_key}&guest_session_id={tc.guest_session_id}'
        payload = {'value': 7.5}
        requests.post(url=request_string, data=payload)

        # Yes, implicit sleeps are bad, but I would flesh something else out had I more time.
        sleep(1)
        # verify this movie is now in the guest's rated movies results
        request_string = tc.base_url + f'/guest_session/{tc.guest_session_id}/rated/movies?api_key={tc.api_key}' \
                                       f'&language=en-US&sort_by=created_at.asc'
        response = requests.get(request_string).json()
        found = False
        for result in response['results']:
            if result['id'] == movie_id:
                found = True
                break
        assert found, f'Movie (id={movie_id}) was not found in guest ratings: {response}'


    @pytest.mark.smoke
    def test_people_search(self, tc: TMDBTestContext):
        """ verify a list of people are returned when searching for an actor """

    @pytest.mark.regression
    def test_add_to_favorites(self, tc):
        """ create session. add movie to favorites, verify movie shows up in user's favorites """
        # TODO: create full user session authentication and framework code for easy login

    @pytest.mark.regression
    def test_delete_from_favorites(self, tc):
        """ add a movie to favorites, delete from favorites, verify deletion """

    @pytest.mark.regression
    def test_create_movie_list(self, tc):
        """ create movie list and verify list was created for that user """

    @pytest.mark.regression
    def test_add_movies_to_list(self, tc):
        """ add multiple movies to list"""

    @pytest.mark.smoke
    def test_movie_search_smoke(self, tc):
        """ verify a movie search returns 200 status code """
        # A HEAD request is sufficient for status codes.

    @pytest.mark.smoke
    def test_create_guest_session_smoke(self, tc):
        """ verify creation of guest session. assert guest session id is returned """

    @pytest.mark.regression
    def test_outdated_session_id(self, tc):
        """ make a request with an outdated session id """

    @pytest.mark.regression
    def test_guest_add_to_favorites(self, tc):
        """ verify guest should not be able to add to favorites """

    @pytest.mark.regression
    def test_invalid_api_key(self, tc):
        """ add a character to a valid key and verify api access is denied """
