from pyblizzard.common.base_community_api import BaseCommunityApi
from pyblizzard.common.utility.urlbuilder import UrlBuilder as UrlBuilder

GAME_NAME = 'd3'

ENDPOINT_PROFILE = 'profile'
ENDPOINT_DATA = 'data'

class Diablo(BaseCommunityApi):
    def __init__(self, api_key, region, locale, timeout):
        self._game = GAME_NAME
        BaseCommunityApi.__init__(self, api_key, region, locale, timeout)

    def get_career_profile(self, battle_tag):
        career_profile_path = UrlBuilder(use_trailing_slash=True) \
            .add(ENDPOINT_PROFILE) \
            .add(battle_tag) \
            .build()
        return self._get_pickled_response_generic(career_profile_path)

    def get_hero_profile(self, battle_tag, hero_id):
        hero_profile_path = UrlBuilder() \
            .add(ENDPOINT_PROFILE) \
            .add(battle_tag) \
            .add('hero') \
            .add(hero_id) \
            .build()
        return self._get_pickled_response_generic(hero_profile_path)

    def get_item_data(self, item_identifier):
        item_data_path = UrlBuilder() \
            .add(ENDPOINT_DATA) \
            .add('item') \
            .add(item_identifier) \
            .build()
        return self._get_pickled_response_generic(item_data_path)

    def get_follower_data(self, follower):
        follower_path = UrlBuilder() \
            .add(ENDPOINT_DATA) \
            .add('follower') \
            .add(follower.value) \
            .build()
        return self._get_pickled_response_generic(follower_path)

    def get_artisan_data(self, artisan):
        print(artisan)
        artisan_path = UrlBuilder() \
            .add(ENDPOINT_DATA) \
            .add('artisan') \
            .add(artisan.value) \
            .build()
        return self._get_pickled_response_generic(artisan_path)
