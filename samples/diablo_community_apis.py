from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.common.utility import util
from pyblizzard.diablo.enum.artisan import Artisan
from pyblizzard.diablo.enum.follower import Follower
from pyblizzard.pyblizzard import PyBlizzard
from samples.config import testconfig

SAMPLE_DIABLO_BATTLE_TAG = 'Spittles-1502'
SAMPLE_DIABLO_HERO_ID = '94825371'
SAMPLE_DIABLO_ITEM_ID = 'Unique_CombatStaff_2H_001_x1'


def main():
    sample_api_key = testconfig.get_api_key()

    py_blizzard = PyBlizzard(sample_api_key, Region.US, Locale.US)

    print('Getting career profile...')
    career_profile = py_blizzard.diablo.get_career_profile(SAMPLE_DIABLO_BATTLE_TAG)
    util.print_response_object(career_profile)

    print('Getting hero profile...')
    hero_profile = py_blizzard.diablo.get_hero_profile(SAMPLE_DIABLO_BATTLE_TAG, SAMPLE_DIABLO_HERO_ID)
    util.print_response_object(hero_profile)

    print('Getting item...')
    item = py_blizzard.diablo.get_item_data(SAMPLE_DIABLO_ITEM_ID)
    util.print_response_object(item)

    print('Getting follower...')
    follower = py_blizzard.diablo.get_follower_data(Follower.ENCHANTRESS)
    util.print_response_object(follower)

    print('Getting artisan...')
    artisan = py_blizzard.diablo.get_artisan_data(Artisan.MYSTIC)
    util.print_response_object(artisan)


if __name__ == '__main__':
    main()
