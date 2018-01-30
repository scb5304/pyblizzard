from pyblizzard.common.base_community_api import BaseCommunityApi
from pyblizzard.common.utility.urlbuilder import UrlBuilder as UrlBuilder

GAME_NAME = 'sc2'

ENDPOINT_PROFILE = 'profile'
ENDPOINT_LADDER = 'ladder'
ENDPOINT_DATA = 'data'

class Starcraft2(BaseCommunityApi):
    def __init__(self, api_key, region, locale, timeout):
        self._game = GAME_NAME
        self._starcraft2_region = '1'  # because I can't find an example online of anyone NOT using 1
        BaseCommunityApi.__init__(self, api_key, region, locale, timeout)

    def get_profile(self, profile_id, profile_name):
        profile_path = UrlBuilder(use_trailing_slash=True) \
            .add(ENDPOINT_PROFILE) \
            .add(profile_id) \
            .add(self._starcraft2_region) \
            .add(profile_name) \
            .build()
        return self._get_pickled_response_generic(profile_path)

    def get_profile_ladders(self, profile_id, profile_name):
        profile_ladders_path = UrlBuilder() \
            .add(ENDPOINT_PROFILE) \
            .add(profile_id) \
            .add(self._starcraft2_region) \
            .add(profile_name) \
            .add('ladders') \
            .build()
        return self._get_pickled_response_generic(profile_ladders_path)

    def get_profile_match_history(self, profile_id, profile_name):
        profile_match_history_path = UrlBuilder() \
            .add(ENDPOINT_PROFILE) \
            .add(profile_id) \
            .add(self._starcraft2_region) \
            .add(profile_name) \
            .add('matches') \
            .build()
        return self._get_pickled_response_generic(profile_match_history_path)

    def get_ladder(self, ladder_id):
        ladder_path = UrlBuilder() \
            .add(ENDPOINT_LADDER) \
            .add(ladder_id) \
            .build()
        return self._get_pickled_response_generic(ladder_path)

    def get_achievements_data(self):
        achievements_path = UrlBuilder() \
            .add(ENDPOINT_DATA) \
            .add('achievements') \
            .build()
        return self._get_pickled_response_generic(achievements_path)

    def get_rewards_data(self):
        rewards_path = UrlBuilder() \
            .add(ENDPOINT_DATA) \
            .add('rewards') \
            .build()
        return self._get_pickled_response_generic(rewards_path)
