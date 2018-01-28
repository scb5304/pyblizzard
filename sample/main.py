import traceback
import jsonpickle
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.diablo.enum.artisan import Artisan
from pyblizzard.diablo.enum.follower import Follower
from pyblizzard.pyblizzard import PyBlizzard
from sample.config import testconfig

SAMPLE_DIABLO_BATTLE_TAG = 'Spittles-1502'
SAMPLE_DIABLO_HERO_ID = '94825371'
SAMPLE_DIABLO_ITEM_ID = 'Unique_CombatStaff_2H_001_x1'

SAMPLE_STARCRAFT2_PROFILE_ID = '2137104'
SAMPLE_STARCRAFT2_PROFILE_NAME = 'skt'
SAMPLE_STARCRAFT2_LADDER_ID = '194163'

def print_result(response_object):
    print(jsonpickle.encode(response_object, unpicklable=False))

def main():
    sample_api_key = None
    try:
        sample_api_key = testconfig.get_api_key()
    except KeyError:
        print('There was an error reading in test\'s config file')
        print(traceback.format_exc())

    if not sample_api_key:
        print('Cannot proceed without an API key.')
        sys.exit(1)

    py_blizzard = PyBlizzard(sample_api_key, Region.US.value, Locale.US.value)

    # DIABLO
    career_profile = py_blizzard.diablo.get_career_profile(SAMPLE_DIABLO_BATTLE_TAG)
    print_result(career_profile)

    hero_profile = py_blizzard.diablo.get_hero_profile(SAMPLE_DIABLO_BATTLE_TAG, SAMPLE_DIABLO_HERO_ID)
    print_result(hero_profile)

    item = py_blizzard.diablo.get_item_data(SAMPLE_DIABLO_ITEM_ID)
    print_result(item)

    follower = py_blizzard.diablo.get_follower_data(Follower.ENCHANTRESS.value)
    print_result(follower)

    artisan = py_blizzard.diablo.get_artisan_data(Artisan.MYSTIC.value)
    print_result(artisan)

    # STARCRAFT2
    profile = py_blizzard.starcraft2.get_profile(SAMPLE_STARCRAFT2_PROFILE_ID, SAMPLE_STARCRAFT2_PROFILE_NAME)
    print_result(profile)

    ladders = py_blizzard.starcraft2.get_profile_ladders(SAMPLE_STARCRAFT2_PROFILE_ID, SAMPLE_STARCRAFT2_PROFILE_NAME)
    print_result(ladders)

    match_history = py_blizzard.starcraft2.get_profile_match_history(SAMPLE_STARCRAFT2_PROFILE_ID, SAMPLE_STARCRAFT2_PROFILE_NAME)
    print_result(match_history)

    ladder = py_blizzard.starcraft2.get_ladder(SAMPLE_STARCRAFT2_LADDER_ID)
    print_result(ladder)

    achievements = py_blizzard.starcraft2.get_achievements_data()
    print_result(achievements)

    rewards = py_blizzard.starcraft2.get_rewards_data()
    print_result(rewards)


if __name__ == '__main__':
    main()
