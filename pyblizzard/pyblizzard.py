from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.diablo.diablo import Diablo
from pyblizzard.starcraft2.starcraft2 import Starcraft2
from pyblizzard.wow.wow import WorldOfWarcraft


class PyBlizzard:
    _api_key = 'NO_API_KEY_PROVIDED'
    _region = Region.US
    _locale = Locale.US
    _timeout = 60

    diablo = None
    starcraft2 = None
    wow = None

    def __init__(self, api_key, region, locale):
        self._api_key = api_key
        self._region = region
        self._locale = locale
        self.diablo = Diablo(api_key, region, locale, self._timeout)
        self.starcraft2 = Starcraft2(api_key, region, locale, self._timeout)
        self.wow = WorldOfWarcraft(api_key, region, locale, self._timeout)

    def set_timeout(self, timeout):
        self._timeout = timeout
        self.diablo.set_timeout(timeout)
        self.starcraft2.set_timeout(timeout)
        self.wow.set_timeout(timeout)
