import requests
from pyblizzard.common.utility import urlbuilder
from pyblizzard.common.constants import url as common_url
from pyblizzard.diablo.constants import segments as diablo_segments


def build_params(locale, api_key):
    return {
        common_url.QUERY_LOCALE: locale,
        common_url.QUERY_API_KEY: api_key
    }


# Note that this call requires a trailing slash.
def get_career_profile(api_key, region, battle_tag, locale):
    diablo_path = build_diablo_path(region)
    career_profile_path = urlbuilder.build_url_from_segments(
        [diablo_path, diablo_segments.ENDPOINT_PROFILE, battle_tag])
    return requests.get(career_profile_path + '/', params=build_params(locale, api_key))


def get_hero_profile(api_key, region, battle_tag, hero_id, locale):
    diablo_path = build_diablo_path(region)
    hero_profile_path = urlbuilder.build_url_from_segments(
        [diablo_path, diablo_segments.ENDPOINT_PROFILE, battle_tag, diablo_segments.HERO, hero_id])
    return requests.get(hero_profile_path, params=build_params(locale, api_key))


def get_item_data(api_key, region, item_identifier, locale):
    diablo_path = build_diablo_path(region)
    item_data_path = urlbuilder.build_url_from_segments(
        [diablo_path, diablo_segments.ENDPOINT_DATA, diablo_segments.ITEM, item_identifier])
    return requests.get(item_data_path, params=build_params(locale, api_key))


def get_follower_data(api_key, region, follower, locale):
    diablo_path = build_diablo_path(region)
    follower_path = urlbuilder.build_url_from_segments(
        [diablo_path, diablo_segments.ENDPOINT_DATA, diablo_segments.FOLLOWER, follower])

    return requests.get(follower_path, params=build_params(locale, api_key))


def get_artisan_data(api_key, region, artisan, locale):
    diablo_path = build_diablo_path(region)
    artisan_path = urlbuilder.build_url_from_segments(
        [diablo_path, diablo_segments.ENDPOINT_DATA, diablo_segments.ARTISAN, artisan])
    return requests.get(artisan_path, params=build_params(locale, api_key))


def build_diablo_path(region):
    base_path = urlbuilder.build_base_path_from_region(region)
    return urlbuilder.build_url_from_segments([base_path, diablo_segments.GAME_NAME])
