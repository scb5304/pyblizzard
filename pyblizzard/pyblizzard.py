from pyblizzard.common.enum.region import Region
from pyblizzard.common.enum.locale import Locale
from pyblizzard.diablo.diablo import Diablo

# Blizzard API root
BLIZZARD_API_ROOT = 'api.battle.net'

# Query param identifiers in requests
QUERY_LOCALE = 'locale'
QUERY_API_KEY = 'apikey'


class PyBlizzard:
    _api_key = 'NO_API_KEY_PROVIDED'
    _region = Region.US.name
    _locale = Locale.US.name
    diablo = None

    def __init__(self, api_key, region, locale):
        self._api_key = api_key
        self._region = region
        self._locale = locale
        self.diablo = Diablo(api_key, region, locale)
