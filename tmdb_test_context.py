import requests


class TMDBTestContext:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url=base_url
        self.guest_session_id = self.create_guest_session()

    def create_guest_session(self):
        response = requests.get(self.base_url + f'/authentication/guest_session/new?api_key={self.api_key}').json()
        return response['guest_session_id']