import pytest

from helpers.api.client import HttpClient
from settings import config


class WikipediaAPI(object):
    API_HOST = config.get('api_host')

    def __init__(self):
        self._http_client = HttpClient(api_host=self.API_HOST)

    @pytest.allure.step
    def suggest(self, query=None, limit=None):
        data = dict(action='opensearch')

        if query:
            data.update({'search': query})

        if limit:
            data.update({'limit': limit})

        return self._http_client.request('/w/api.php', method='GET', data=data)


wikipedia_api = WikipediaAPI()
