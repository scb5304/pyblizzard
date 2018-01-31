import jsonpickle
import requests
from pyblizzard.common.utility.urlbuilder import UrlBuilder


class BaseCommunityApi:
    BLIZZARD_API_ROOT = 'api.battle.net'
    QUERY_LOCALE = 'locale'
    QUERY_API_KEY = 'apikey'

    def _init_params(self):
        self._params = {self.QUERY_LOCALE: self._locale.value, self.QUERY_API_KEY: self._api_key}

    def __init__(self, api_key, region, locale, timeout):
        self._api_key = api_key
        self._region = region
        self._locale = locale
        self._timeout = timeout
        self._base_game_api_path = self.build_base_api_path()
        self._init_params()
        self._game = None

    def set_timeout(self, timeout):
        self._timeout = timeout

    def build_base_api_path(self):
        base_blizzard_path = 'https://{}.{}'.format(self._region.value, self.BLIZZARD_API_ROOT)
        return UrlBuilder() \
            .add(base_blizzard_path) \
            .add(self._game) \
            .build()

    def _get_pickled_response_generic(self, path):
        full_path = UrlBuilder() \
            .add(self._base_game_api_path) \
            .add(path) \
            .build()
        response = requests.get(full_path, params=self._params, timeout=self._timeout)
        self._init_params()
        return jsonpickle.decode(response.text)
