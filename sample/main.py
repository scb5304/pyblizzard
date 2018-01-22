from sample.config import testconfig
from pyblizzard.diablo import diablo
from pyblizzard.diablo.constants import followers
from pyblizzard.diablo.constants import artisans
from pyblizzard.common.constants import regions
from pyblizzard.common.constants import locales

import traceback

test_api_key = None

try:
    test_api_key = testconfig.get_api_key()
except KeyError:
    print('There was an error reading in test\'s config file')
    print(traceback.format_exc())

if not test_api_key:
    print('Cannot proceed without an API key')

career_response = diablo.get_career_profile(test_api_key, regions.US, 'Spittles-1502', locales.US)
print(career_response.url)
print(career_response.status_code)
# print(career_response.text)

hero_response = diablo.get_hero_profile(test_api_key, regions.US, 'Spittles-1502', '94825371', locales.US)
print(hero_response.url)
print(hero_response.status_code)
# print(hero_response.text)

item_response = diablo.get_item_data(test_api_key, regions.US, 'Crossbow_001', locales.US)
print(item_response.url)
print(item_response.status_code)
# print(item_response.text)

follower_response = diablo.get_follower_data(test_api_key, regions.US, followers.ENCHANTRESS, locales.US)
print(follower_response.url)
print(follower_response.status_code)
# print(follower_response.text)

artisan_response = diablo.get_artisan_data(test_api_key, regions.US, artisans.MYSTIC, locales.US)
print(artisan_response.url)
print(artisan_response.status_code)
# print(artisan_response.text)