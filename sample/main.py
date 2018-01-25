import traceback
import jsonpickle

from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.diablo.models.artisan import Artisan
from pyblizzard.diablo.models.follower import Follower
from pyblizzard.pyblizzard import PyBlizzard
from sample.config import testconfig

SAMPLE_API_KEY = None
SAMPLE_BATTLE_TAG = 'Spittles-1502'
SAMPLE_HERO_ID = '94825371'
SAMPLE_ITEM_ID = 'Unique_CombatStaff_2H_001_x1'

try:
    SAMPLE_API_KEY = testconfig.get_api_key()
except KeyError:
    print('There was an error reading in test\'s config file')
    print(traceback.format_exc())

if not SAMPLE_API_KEY:
    print('Cannot proceed without an API key')

py_blizzard = PyBlizzard(SAMPLE_API_KEY, Region.US.name, Locale.US.name)

career_profile = py_blizzard.diablo.get_career_profile(SAMPLE_BATTLE_TAG)
print(jsonpickle.encode(career_profile, unpicklable=False))

hero_profile = py_blizzard.diablo.get_hero_profile(SAMPLE_BATTLE_TAG, SAMPLE_HERO_ID)
print(jsonpickle.encode(hero_profile, unpicklable=False))

item = py_blizzard.diablo.get_item_data(SAMPLE_ITEM_ID)
print(jsonpickle.encode(item, unpicklable=False))

follower = py_blizzard.diablo.get_follower_data(Follower.ENCHANTRESS)
print(jsonpickle.encode(follower, unpicklable=False))

artisan = py_blizzard.diablo.get_artisan_data(Artisan.MYSTIC)
print(jsonpickle.encode(artisan, unpicklable=False))
