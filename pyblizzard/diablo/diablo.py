import requests
from pyblizzard.common.utility import urlbuilder
from pyblizzard.common.constants import url as common_url
from pyblizzard.diablo.constants import segments as diablo_segments


# Example: https://us.api.battle.net/d3/profile/Spittles-1502/?locale=en_US&apikey=api_key
def get_career_profile(api_key, region, battle_tag, locale):
    diablo_path = build_diablo_path(region)
    career_profile_path = urlbuilder.build_url_from_segments([diablo_path, diablo_segments.CAREER_PROFILE, battle_tag])
    params = {
        common_url.QUERY_LOCALE: locale,
        common_url.QUERY_API_KEY: api_key
    }
    return requests.get(career_profile_path, params=params)


def build_diablo_path(region):
    base_path = urlbuilder.build_base_path_from_region(region)
    return urlbuilder.build_url_from_segments([base_path, diablo_segments.GAME_NAME])
