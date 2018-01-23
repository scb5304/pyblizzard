import traceback

import jsonpickle

from pyblizzard.common.constants import locales
from pyblizzard.common.constants import regions
from pyblizzard.diablo import diablo
from pyblizzard.diablo.constants import artisans
from pyblizzard.diablo.constants import followers
from sample.config import testconfig

test_api_key = None

try:
    test_api_key = testconfig.get_api_key()
except KeyError:
    print('There was an error reading in test\'s config file')
    print(traceback.format_exc())

if not test_api_key:
    print('Cannot proceed without an API key')

career_profile = diablo.get_career_profile(test_api_key, regions.US, 'Spittles-1502', locales.US)
print(jsonpickle.encode(career_profile, unpicklable=False))

hero_profile = diablo.get_hero_profile(test_api_key, regions.US, 'Spittles-1502', '94825371', locales.US)
print(jsonpickle.encode(hero_profile, unpicklable=False))

item = diablo.get_item_data(test_api_key, regions.US, 'Unique_CombatStaff_2H_001_x1', locales.US)
print(jsonpickle.encode(item, unpicklable=False))

follower = diablo.get_follower_data(test_api_key, regions.US, followers.ENCHANTRESS, locales.US)
print(jsonpickle.encode(follower, unpicklable=False))

artisan = diablo.get_artisan_data(test_api_key, regions.US, artisans.MYSTIC, locales.US)
print(jsonpickle.encode(artisan, unpicklable=False))
