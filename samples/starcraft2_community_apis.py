from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.common.utility import util

from pyblizzard.pyblizzard import PyBlizzard
from samples.config import testconfig

SAMPLE_STARCRAFT2_PROFILE_ID = '2137104'
SAMPLE_STARCRAFT2_PROFILE_NAME = 'skt'
SAMPLE_STARCRAFT2_LADDER_ID = '194163'

def main():
    sample_api_key = testconfig.get_api_key()

    py_blizzard = PyBlizzard(sample_api_key, Region.US, Locale.US)

    print('Getting profile...')
    profile = py_blizzard.starcraft2.get_profile(SAMPLE_STARCRAFT2_PROFILE_ID, SAMPLE_STARCRAFT2_PROFILE_NAME)
    util.print_response_object(profile)

    print('Getting ladders...')
    ladders = py_blizzard.starcraft2.get_profile_ladders(SAMPLE_STARCRAFT2_PROFILE_ID, SAMPLE_STARCRAFT2_PROFILE_NAME)
    util.print_response_object(ladders)

    print('Getting match history...')
    match_history = py_blizzard.starcraft2.get_profile_match_history(SAMPLE_STARCRAFT2_PROFILE_ID, SAMPLE_STARCRAFT2_PROFILE_NAME)
    util.print_response_object(match_history)

    print('Getting ladder...')
    ladder = py_blizzard.starcraft2.get_ladder(SAMPLE_STARCRAFT2_LADDER_ID)
    util.print_response_object(ladder)

    print('Getting achievements...')
    achievements = py_blizzard.starcraft2.get_achievements_data()
    util.print_response_object(achievements)

    print('Getting rewards...')
    rewards = py_blizzard.starcraft2.get_rewards_data()
    util.print_response_object(rewards)


if __name__ == '__main__':
    main()
