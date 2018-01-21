import leahconfig
import traceback

leah_api_key = None

try:
    leah_api_key = leahconfig.get_api_key()
except KeyError:
    print('There was an error reading in Leah\'s config file')
    print(traceback.format_exc())

if leah_api_key:
    print(leah_api_key)
else:
    print('Cannot proceed without an API key')

