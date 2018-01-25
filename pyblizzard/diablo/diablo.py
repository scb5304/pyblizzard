import json

import requests

from pyblizzard import pyblizzard
from pyblizzard.common.utility.urlbuilder import UrlBuilder as UrlBuilder
from pyblizzard.diablo.models.artisan import Artisan
from pyblizzard.diablo.models.careerprofile import CareerProfile
from pyblizzard.diablo.models.follower import Follower
from pyblizzard.diablo.models.heroprofile import HeroProfile
from pyblizzard.diablo.models.item import Item

GAME_NAME = 'd3'

ENDPOINT_PROFILE = 'profile'
ENDPOINT_DATA = 'data'

HERO = 'hero'
ITEM = 'item'
FOLLOWER = 'follower'
ARTISAN = 'artisan'


class Diablo:
    def __init__(self, api_key, region, locale):
        self._api_key = api_key
        self._region = region
        self._locale = locale

    @staticmethod
    def build_base_path_from_region(region):
        return 'https://{}.{}'.format(region, pyblizzard.BLIZZARD_API_ROOT)

    @staticmethod
    def build_diablo_path(region):
        base_blizzard_path = Diablo.build_base_path_from_region(region)
        return UrlBuilder() \
            .add(base_blizzard_path) \
            .add(GAME_NAME) \
            .build()

    def make_diablo_request(self, path):
        base_diablo_path = self.build_diablo_path(self._region)
        full_url = UrlBuilder() \
            .add(base_diablo_path) \
            .add(path) \
            .build()
        print('Built URL for Diablo request: ', full_url)

        return requests.get(full_url, params={pyblizzard.QUERY_LOCALE: self._locale, pyblizzard.QUERY_API_KEY: self._api_key})

    def get_career_profile(self, battle_tag):
        career_profile_path = UrlBuilder(use_trailing_slash=True) \
            .add(ENDPOINT_PROFILE) \
            .add(battle_tag) \
            .build()
        request_result = self.make_diablo_request(career_profile_path)
        return CareerProfile(**json.loads(request_result.text))

    def get_hero_profile(self, battle_tag, hero_id):
        hero_profile_path = UrlBuilder() \
            .add(ENDPOINT_PROFILE) \
            .add(battle_tag) \
            .add(HERO) \
            .add(hero_id) \
            .build()
        request_result = self.make_diablo_request(hero_profile_path)
        return HeroProfile(**json.loads(request_result.text))

    def get_item_data(self, item_identifier):
        item_data_path = UrlBuilder() \
            .add(ENDPOINT_DATA) \
            .add(ITEM) \
            .add(item_identifier) \
            .build()
        request_result = self.make_diablo_request(item_data_path)
        return Item(**json.loads(request_result.text))

    def get_follower_data(self, follower):
        follower_path = UrlBuilder() \
            .add(ENDPOINT_DATA) \
            .add(FOLLOWER) \
            .add(follower) \
            .build()
        request_result = self.make_diablo_request(follower_path)
        return Follower(**json.loads(request_result.text))

    def get_artisan_data(self, artisan):
        artisan_path = UrlBuilder() \
            .add(ENDPOINT_DATA) \
            .add(ARTISAN) \
            .add(artisan) \
            .build()
        request_result = self.make_diablo_request(artisan_path)
        return Artisan(**json.loads(request_result.text))