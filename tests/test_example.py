import pytest

from helpers.api.wikipedia_api import wikipedia_api


@pytest.mark.categories(component='suggest', suite='smoke')
@pytest.allure.feature('GET /w/api.php?action=opensearch')
class TestWikipediaSuggest(object):
    @pytest.mark.parametrize("query", ('python', 'rest', 'query'))
    def test_suggest_query(self, query):
        response = wikipedia_api.suggest(query=query)
        assert response.status_code == 200, 'Expected 200 status_code, but actual is %d' % response.status_code

        response = response.json()
        assert isinstance(response, list), 'Expected `list` response object type, but actual is %s' % type(response)
        assert (all(query.lower() in r.lower() for r in response[1]),
                'Not all suggestions has %s value in result' % query)
