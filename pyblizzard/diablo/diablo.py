import requests
import json

from pyblizzard.common.utility import util
from pyblizzard.common.constants import url as common_url
from pyblizzard.diablo.constants import segments as diablo_segments
from pyblizzard.diablo.models.item import Item
from pyblizzard.diablo.models.follower import Follower
from pyblizzard.diablo.models.artisan import Artisan
from pyblizzard.diablo.models.heroprofile import HeroProfile
from pyblizzard.diablo.models.careerprofile import CareerProfile
from pyblizzard.common.utility.urlbuilder import UrlBuilder as UrlBuilder


def build_params(locale, api_key):
    return {
        common_url.QUERY_LOCALE: locale,
        common_url.QUERY_API_KEY: api_key
    }


def get_career_profile(api_key, region, battle_tag, locale):
    career_profile_path = UrlBuilder(use_trailing_slash=True) \
        .add(diablo_segments.ENDPOINT_PROFILE) \
        .add(battle_tag) \
        .build()
    request_result = make_diablo_request(career_profile_path, region, locale, api_key)
    return CareerProfile(**json.loads(request_result.text))


def get_hero_profile(api_key, region, battle_tag, hero_id, locale):
    hero_profile_path = UrlBuilder() \
        .add(diablo_segments.ENDPOINT_PROFILE) \
        .add(battle_tag) \
        .add(diablo_segments.HERO) \
        .add(hero_id) \
        .build()
    request_result = make_diablo_request(hero_profile_path, region, locale, api_key)
    return HeroProfile(**json.loads(request_result.text))


def get_item_data(api_key, region, item_identifier, locale):
    item_data_path = UrlBuilder() \
        .add(diablo_segments.ENDPOINT_DATA) \
        .add(diablo_segments.ITEM) \
        .add(item_identifier) \
        .build()
    request_result = make_diablo_request(item_data_path, region, locale, api_key)
    return Item(**json.loads(request_result.text))


def get_follower_data(api_key, region, follower, locale):
    follower_path = UrlBuilder() \
        .add(diablo_segments.ENDPOINT_DATA) \
        .add(diablo_segments.FOLLOWER) \
        .add(follower) \
        .build()
    request_result = make_diablo_request(follower_path, region, locale, api_key)
    return Follower(**json.loads(request_result.text))


def get_artisan_data(api_key, region, artisan, locale):
    artisan_path = UrlBuilder() \
        .add(diablo_segments.ENDPOINT_DATA) \
        .add(diablo_segments.ARTISAN) \
        .add(artisan) \
        .build()
    request_result = make_diablo_request(artisan_path, region, locale, api_key)
    return Artisan(**json.loads(request_result.text))


def build_diablo_path(region):
    base_blizzard_path = util.build_base_path_from_region(region)
    return UrlBuilder() \
        .add(base_blizzard_path) \
        .add(diablo_segments.GAME_NAME) \
        .build()


def make_diablo_request(path, region, locale, api_key):
    base_diablo_path = build_diablo_path(region)

    full_url = UrlBuilder() \
        .add(base_diablo_path) \
        .add(path) \
        .build()

    print('Built URL for Diablo request: ', full_url)
    return requests.get(full_url, params=build_params(locale, api_key))
