import re

import pytest
import responses

from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.starcraft2.starcraft2 import Starcraft2

TEST_API_KEY = 'abc123'
TEST_REGION = Region.US
TEST_LOCALE = Locale.US
TEST_TIMEOUT = 1.0

TEST_STARCRAFT2_PROFILE_ID = '2137104'
TEST_STARCRAFT2_PROFILE_NAME = 'skt'
TEST_STARCRAFT2_LADDER_ID = '194163'

@pytest.fixture()
def stub_request_empty_json():
    responses.add(responses.GET, re.compile('.+'), json={})

@pytest.mark.usefixtures("stub_request_empty_json")
class TestStarcraft2:

    @staticmethod
    def create_test_starcraft2_instance():
        return Starcraft2(TEST_API_KEY, TEST_REGION, TEST_LOCALE, TEST_TIMEOUT)

    @responses.activate
    def test_get_profile(self):
        """get_profile sends a request with the expected URL."""
        starcraft2 = self.create_test_starcraft2_instance()
        starcraft2.get_profile(TEST_STARCRAFT2_PROFILE_ID, TEST_STARCRAFT2_PROFILE_NAME)

        expected_url = 'https://us.api.battle.net/sc2/profile/2137104/1/skt/?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_profile_ladders(self):
        """get_profile_ladders sends a request with the expected URL."""
        starcraft2 = self.create_test_starcraft2_instance()
        starcraft2.get_profile_ladders(TEST_STARCRAFT2_PROFILE_ID, TEST_STARCRAFT2_PROFILE_NAME)

        expected_url = 'https://us.api.battle.net/sc2/profile/2137104/1/skt/ladders?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_profile_match_history(self):
        """get_profile_match_history sends a request with the expected URL."""
        starcraft2 = self.create_test_starcraft2_instance()
        starcraft2.get_profile_match_history(TEST_STARCRAFT2_PROFILE_ID, TEST_STARCRAFT2_PROFILE_NAME)

        expected_url = 'https://us.api.battle.net/sc2/profile/2137104/1/skt/matches?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_ladder(self):
        """get_ladder sends a request with the expected URL."""
        starcraft2 = self.create_test_starcraft2_instance()
        starcraft2.get_ladder(TEST_STARCRAFT2_LADDER_ID)

        expected_url = 'https://us.api.battle.net/sc2/ladder/194163?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_achievements_data(self):
        """get_achievements_data sends a request with the expected URL."""
        starcraft2 = self.create_test_starcraft2_instance()
        starcraft2.get_achievements_data()

        expected_url = 'https://us.api.battle.net/sc2/data/achievements?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_rewards_data(self):
        """get_rewards_data sends a request with the expected URL."""
        starcraft2 = self.create_test_starcraft2_instance()
        starcraft2.get_rewards_data()

        expected_url = 'https://us.api.battle.net/sc2/data/rewards?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url
