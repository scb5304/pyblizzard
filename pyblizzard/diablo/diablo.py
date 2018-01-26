import json
import logging
import requests

from pyblizzard import pyblizzard
from pyblizzard.common.utility import util
from pyblizzard.common.utility.urlbuilder import UrlBuilder as UrlBuilder
from pyblizzard.diablo.models.artisan import Artisan
from pyblizzard.diablo.models.careerprofile import CareerProfile
from pyblizzard.diablo.models.follower import Follower
from pyblizzard.diablo.models.heroprofile import HeroProfile
from pyblizzard.diablo.models.item import Item

logging.basicConfig(level=logging.DEBUG)

GAME_NAME = 'd3'

ENDPOINT_PROFILE = 'profile'
ENDPOINT_DATA = 'data'

HERO = 'hero'
ITEM = 'item'
FOLLOWER = 'follower'
ARTISAN = 'artisan'


class Diablo:
    def build_diablo_path(self):
        base_blizzard_path = util.build_base_path_from_region(self._region)
        return UrlBuilder() \
            .add(base_blizzard_path) \
            .add(GAME_NAME) \
            .build()

    def __init__(self, api_key, region, locale, timeout):
        self._api_key = api_key
        self._region = region
        self._locale = locale
        self._timeout = timeout
        self._base_diablo_path = self.build_diablo_path()
        self._params = {pyblizzard.QUERY_LOCALE: self._locale, pyblizzard.QUERY_API_KEY: self._api_key}

    def set_timeout(self, timeout):
        self._timeout = timeout

    def _get_diablo_generic(self, path, class_):
        full_path = UrlBuilder() \
            .add(self._base_diablo_path) \
            .add(path) \
            .build()
        response = requests.get(full_path, params=self._params, timeout=self._timeout)
        model_object = class_(**json.loads(response.text))
        return model_object

    def get_career_profile(self, battle_tag):
        career_profile_path = UrlBuilder(use_trailing_slash=True) \
            .add(ENDPOINT_PROFILE) \
            .add(battle_tag) \
            .build()
        return self._get_diablo_generic(career_profile_path, CareerProfile)

    def get_hero_profile(self, battle_tag, hero_id):
        hero_profile_path = UrlBuilder() \
            .add(ENDPOINT_PROFILE) \
            .add(battle_tag) \
            .add(HERO) \
            .add(hero_id) \
            .build()
        return self._get_diablo_generic(hero_profile_path, HeroProfile)

    def get_item_data(self, item_identifier):
        item_data_path = UrlBuilder() \
            .add(ENDPOINT_DATA) \
            .add(ITEM) \
            .add(item_identifier) \
            .build()
        return self._get_diablo_generic(item_data_path, Item)

    def get_follower_data(self, follower):
        follower_path = UrlBuilder() \
            .add(ENDPOINT_DATA) \
            .add(FOLLOWER) \
            .add(follower) \
            .build()
        return self._get_diablo_generic(follower_path, Follower)

    def get_artisan_data(self, artisan):
        artisan_path = UrlBuilder() \
            .add(ENDPOINT_DATA) \
            .add(ARTISAN) \
            .add(artisan) \
            .build()
        return self._get_diablo_generic(artisan_path, Artisan)
