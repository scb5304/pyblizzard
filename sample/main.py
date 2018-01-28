import traceback
import jsonpickle
import sys

from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.diablo.enum.artisan import Artisan
from pyblizzard.diablo.enum.follower import Follower
from pyblizzard.pyblizzard import PyBlizzard
from sample.config import testconfig

SAMPLE_BATTLE_TAG = 'Spittles-1502'
SAMPLE_HERO_ID = '94825371'
SAMPLE_ITEM_ID = 'Unique_CombatStaff_2H_001_x1'

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

    career_profile = py_blizzard.diablo.get_career_profile(SAMPLE_BATTLE_TAG)
    print(jsonpickle.encode(career_profile, unpicklable=False))

    hero_profile = py_blizzard.diablo.get_hero_profile(SAMPLE_BATTLE_TAG, SAMPLE_HERO_ID)
    print(jsonpickle.encode(hero_profile, unpicklable=False))

    item = py_blizzard.diablo.get_item_data(SAMPLE_ITEM_ID)
    print(jsonpickle.encode(item, unpicklable=False))

    follower = py_blizzard.diablo.get_follower_data(Follower.ENCHANTRESS.value)
    print(jsonpickle.encode(follower, unpicklable=False))

    artisan = py_blizzard.diablo.get_artisan_data(Artisan.MYSTIC.value)
    print(jsonpickle.encode(artisan, unpicklable=False))


if __name__ == '__main__':
    main()
