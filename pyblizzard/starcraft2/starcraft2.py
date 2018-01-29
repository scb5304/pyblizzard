import jsonpickle
import requests

from pyblizzard import pyblizzard
from pyblizzard.common.utility import util
from pyblizzard.common.utility.urlbuilder import UrlBuilder as UrlBuilder

GAME_NAME = 'sc2'

ENDPOINT_PROFILE = 'profile'
ENDPOINT_LADDER = 'ladder'
ENDPOINT_DATA = 'data'

class Starcraft2:
    def build_starcraft2_path(self):
        base_blizzard_path = util.build_base_path_from_region(self._region)
        return UrlBuilder() \
            .add(base_blizzard_path) \
            .add(GAME_NAME) \
            .build()

    def __init__(self, api_key, region, locale, timeout):
        self._api_key = api_key
        self._region = region
        self._starcraft2_region = '1'  # because I can't find an example online of anyone NOT using 1
        self._locale = locale
        self._timeout = timeout
        self._base_starcraft2_path = self.build_starcraft2_path()
        self._params = {pyblizzard.QUERY_LOCALE: self._locale, pyblizzard.QUERY_API_KEY: self._api_key}

    def set_timeout(self, timeout):
        self._timeout = timeout

    def _get_starcraft2_generic(self, path):
        full_path = UrlBuilder() \
            .add(self._base_starcraft2_path) \
            .add(path) \
            .build()
        response = requests.get(full_path, params=self._params, timeout=self._timeout)
        return jsonpickle.decode(response.text)

    def get_profile(self, profile_id, profile_name):
        profile_path = UrlBuilder(use_trailing_slash=True) \
            .add(ENDPOINT_PROFILE) \
            .add(profile_id) \
            .add(self._starcraft2_region) \
            .add(profile_name) \
            .build()
        return self._get_starcraft2_generic(profile_path)

    def get_profile_ladders(self, profile_id, profile_name):
        profile_ladders_path = UrlBuilder() \
            .add(ENDPOINT_PROFILE) \
            .add(profile_id) \
            .add(self._starcraft2_region) \
            .add(profile_name) \
            .add('ladders') \
            .build()
        return self._get_starcraft2_generic(profile_ladders_path)

    def get_profile_match_history(self, profile_id, profile_name):
        profile_match_history_path = UrlBuilder() \
            .add(ENDPOINT_PROFILE) \
            .add(profile_id) \
            .add(self._starcraft2_region) \
            .add(profile_name) \
            .add('matches') \
            .build()
        return self._get_starcraft2_generic(profile_match_history_path)

    def get_ladder(self, ladder_id):
        ladder_path = UrlBuilder() \
            .add(ENDPOINT_LADDER) \
            .add(ladder_id) \
            .build()
        return self._get_starcraft2_generic(ladder_path)

    def get_achievements_data(self):
        achievements_path = UrlBuilder() \
            .add(ENDPOINT_DATA) \
            .add('achievements') \
            .build()
        return self._get_starcraft2_generic(achievements_path)

    def get_rewards_data(self):
        rewards_path = UrlBuilder() \
            .add(ENDPOINT_DATA) \
            .add('rewards') \
            .build()
        return self._get_starcraft2_generic(rewards_path)