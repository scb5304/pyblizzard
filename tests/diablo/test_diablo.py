import re
import responses

from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.diablo.diablo import Diablo, ENDPOINT_DATA, ITEM
from pyblizzard.diablo.models.item import Item

TEST_API_KEY = 'abc123'
TEST_REGION = Region.US.name
TEST_LOCALE = Locale.US.name
TEST_TIMEOUT = 1.0

TEST_ITEM_ID = 'Unique_CombatStaff_2H_001_x1'

class TestDiablo:

    @responses.activate
    def test_get_item_data_url(self):
        """Assert that get_item_data assembles a URL with necessary data to fetch the response from Blizzard."""
        responses.add(responses.GET, re.compile('.+'), json={})
        diablo = Diablo(TEST_API_KEY, TEST_REGION, TEST_LOCALE, TEST_TIMEOUT)
        diablo.get_item_data(TEST_ITEM_ID)

        request = responses.calls[0].request
        assert TEST_REGION in request.url
        assert TEST_LOCALE in request.url
        assert TEST_API_KEY in request.url
        assert TEST_ITEM_ID in request.url
        assert ENDPOINT_DATA in request.url
        assert ITEM in request.url

    def test_get_item_data_returns_item(self):
        """Assert that get_item_data assembles the returned response into an Item instance."""
        responses.add(responses.GET, re.compile('.+'), json={})
        diablo = Diablo(TEST_API_KEY, TEST_REGION, TEST_LOCALE, TEST_TIMEOUT)
        item = diablo.get_item_data(TEST_ITEM_ID)

        assert isinstance(item, Item)
