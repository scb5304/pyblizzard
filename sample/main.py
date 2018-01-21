from sample.config import testconfig
from pyblizzard.diablo import diablo
from pyblizzard.common.constants import region
from pyblizzard.common.constants import locale
import traceback

test_api_key = None

try:
    test_api_key = testconfig.get_api_key()
except KeyError:
    print('There was an error reading in test\'s config file')
    print(traceback.format_exc())

if not test_api_key:
    print('Cannot proceed without an API key')

career_response = diablo.get_career_profile(test_api_key, region.US, 'Spittles-1502', locale.US)
print(career_response.url)
print(career_response.text)