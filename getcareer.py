import requests
from requests.compat import urljoin

base_diablo_profile_url = 'https://us.api.battle.net/d3/profile/'
locale = 'en_US'

def get_spittles_career(api_key, battletag):
    params = {'locale': locale, 'apikey': api_key}
    request_url = requests.compat.urljoin(base_diablo_profile_url, battletag) + '/'
    return requests.get(request_url, params=params)

