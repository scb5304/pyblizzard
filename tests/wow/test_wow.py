import re

import pytest
import responses

from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.wow.enum.characterprofilefield import CharacterProfileField
from pyblizzard.wow.enum.guildprofilefield import GuildProfileField
from pyblizzard.wow.enum.pvpbracket import PvpBracket
from pyblizzard.wow.wow import WorldOfWarcraft

TEST_API_KEY = 'abc123'
TEST_REGION = Region.US.value
TEST_LOCALE = Locale.US.value
TEST_TIMEOUT = 1.0

TEST_WOW_ACHIEVEMENT_ID = '2144'
TEST_WOW_GUILD_NAME = 'Basement Dwellers'
TEST_WOW_REALM = 'Emerald Dream'
TEST_WOW_CHARACTER_NAME = 'Spittles'
TEST_WOW_BOSS_ID = '24723'
TEST_WOW_ITEM_ID = '18803'
TEST_WOW_ITEM_SET_ID = '1060'
TEST_WOW_PET_ABILITY_ID = '640'
TEST_WOW_PET_SPECIES_ID = '258'
TEST_WOW_QUEST_ID = '13146'
TEST_WOW_RECIPE_ID = '33994'
TEST_WOW_SPELL_ID = '8056'
TEST_WOW_ZONE_ID = '4131'

@pytest.fixture()
def stub_request_empty_json():
    responses.add(responses.GET, re.compile('.+'), json={})

@pytest.mark.usefixtures("stub_request_empty_json")
class TestWorldOfWarcraft:

    @staticmethod
    def create_test_world_of_warcraft_instance():
        return WorldOfWarcraft(TEST_API_KEY, TEST_REGION, TEST_LOCALE, TEST_TIMEOUT)

    # ACHIEVEMENT
    @responses.activate
    def test_get_achievement(self):
        """get_achievement sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_achievement(TEST_WOW_ACHIEVEMENT_ID)

        expected_url = 'https://us.api.battle.net/wow/achievement/2144?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    # AUCTION DATA
    @responses.activate
    def test_get_auction_house(self):
        """get_achievement sends two requests with the expected URL."""
        responses.reset()
        expected_url_one = 'https://us.api.battle.net/wow/auction/data/Emerald%20Dream?locale=en_US&apikey=abc123'
        expected_url_two = 'http://auction-api-us.worldofwarcraft.com/auction-data/82affd1bb4efb4f62c8cf6c511bf642e/auctions.json'

        # Stub twice as we expect two requests.
        responses.add(responses.GET, re.compile('.+'), json={'files': [{'lastModified': 1516113044000, 'url': expected_url_two}]})
        responses.add(responses.GET, re.compile('.+'), json='')

        wow = self.create_test_world_of_warcraft_instance()
        wow.get_auction_data(TEST_WOW_REALM)

        request_one = responses.calls[0].request
        request_two = responses.calls[1].request

        assert request_one.url == expected_url_one
        assert request_two.url == expected_url_two

    # BOSS
    @responses.activate
    def test_get_bosses(self):
        """get_bosses sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_bosses()

        expected_url = 'https://us.api.battle.net/wow/boss/?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_boss(self):
        """get_achievement sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_boss(TEST_WOW_BOSS_ID)

        expected_url = 'https://us.api.battle.net/wow/boss/24723?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    # CHALLENGE
    @responses.activate
    def test_get_realm_challenge_leaderboard(self):
        """get_realm_challenge_leaderboard sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_realm_challenge_leaderboard(TEST_WOW_REALM)

        expected_url = 'https://us.api.battle.net/wow/challenge/Emerald%20Dream?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_region_challenge_leaderboard(self):
        """get_region_challenge_leaderboard sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_region_challenge_leaderboard()

        expected_url = 'https://us.api.battle.net/wow/challenge/region?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    # CHARACTER PROFILE
    @responses.activate
    def test_get_character_profile_no_args(self):
        """get_character_profile sends a request with the expected URL when no args."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_character_profile(TEST_WOW_REALM, TEST_WOW_CHARACTER_NAME)

        expected_url = 'https://us.api.battle.net/wow/character/Emerald%20Dream/Spittles?locale=en_US&apikey=abc123&fields=achievements+appearance+feed+guild+hunterPets+items+mounters+pets+petSlots+professions+progression+pvp+quests+reputation+statistics+stats+talents+titles+audit'
        request = responses.calls[0].request
        print(request.url)
        assert request.url == expected_url

    @responses.activate
    def test_get_character_profile_args(self):
        """get_character_profile sends a request with the expected URL when args."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_character_profile(TEST_WOW_REALM, TEST_WOW_CHARACTER_NAME, CharacterProfileField.ACHIEVEMENTS, CharacterProfileField.FEED)

        expected_url = 'https://us.api.battle.net/wow/character/Emerald%20Dream/Spittles?locale=en_US&apikey=abc123&fields=achievements+feed'
        request = responses.calls[0].request
        print(request.url)
        assert request.url == expected_url

    # GUILD PROFILE
    @responses.activate
    def test_get_guild_profile_no_args(self):
        """get_guild_profile sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_guild_profile(TEST_WOW_REALM, TEST_WOW_GUILD_NAME)

        expected_url = 'https://us.api.battle.net/wow/guild/Emerald%20Dream/Basement%20Dwellers?locale=en_US&apikey=abc123&fields=achievements+members+news+challenge'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_guild_profile_args(self):
        """get_guild_profile sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_guild_profile(TEST_WOW_REALM, TEST_WOW_GUILD_NAME, GuildProfileField.ACHIEVEMENTS, GuildProfileField.NEWS, GuildProfileField.CHALLENGE)

        expected_url = 'https://us.api.battle.net/wow/guild/Emerald%20Dream/Basement%20Dwellers?locale=en_US&apikey=abc123&fields=achievements+news+challenge'
        request = responses.calls[0].request
        assert request.url == expected_url

    # ITEM
    @responses.activate
    def test_get_item(self):
        """get_item sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_item(TEST_WOW_ITEM_ID)

        expected_url = 'https://us.api.battle.net/wow/item/18803?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_item_set(self):
        """get_item_set sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_item_set(TEST_WOW_ITEM_SET_ID)

        expected_url = 'https://us.api.battle.net/wow/item/set/1060?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    # MOUNT
    @responses.activate
    def test_get_mounts(self):
        """get_mounts sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_mounts()

        expected_url = 'https://us.api.battle.net/wow/mount/?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    # PET
    @responses.activate
    def test_get_pets(self):
        """get_pets sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_pets()

        expected_url = 'https://us.api.battle.net/wow/pet?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_pet_ability(self):
        """get_pet_ability sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_pet_ability(TEST_WOW_PET_ABILITY_ID)

        expected_url = 'https://us.api.battle.net/wow/pet/ability/640?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_pet_species(self):
        """get_pet_species sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_pet_species(TEST_WOW_PET_SPECIES_ID)

        expected_url = 'https://us.api.battle.net/wow/pet/species/258?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_pet_stats_by_species(self):
        """get_pet_stats_by_species sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_pet_stats_by_species(TEST_WOW_PET_SPECIES_ID)

        expected_url = 'https://us.api.battle.net/wow/pet/stats/258?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    # PVP
    @responses.activate
    def test_get_pvp_leaderboard_for_bracket(self):
        """get_pvp_leaderboard_for_bracket sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_pvp_leaderboard_for_bracket(PvpBracket.two_v_two)

        expected_url = 'https://us.api.battle.net/wow/leaderboard/2v2?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    # QUEST
    @responses.activate
    def test_get_quest(self):
        """get_quest sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_quest(TEST_WOW_QUEST_ID)

        expected_url = 'https://us.api.battle.net/wow/quest/13146?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    # REALM STATUS
    @responses.activate
    def test_get_realm_status_no_args(self):
        """get_realm_status sends a request with the expected URL when no args."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_realm_status()

        expected_url = 'https://us.api.battle.net/wow/realm/status?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_realm_status_args(self):
        """get_realm_status sends a request with the expected URL when args."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_realm_status(limit_to_realms=['aegwynn', 'aerie-peak'])

        expected_url = 'https://us.api.battle.net/wow/realm/status?locale=en_US&apikey=abc123&realms=aegwynn+aerie-peak'
        request = responses.calls[0].request
        assert request.url == expected_url

    # RECIPE
    @responses.activate
    def test_get_recipe(self):
        """get_recipe sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_recipe(TEST_WOW_RECIPE_ID)

        expected_url = 'https://us.api.battle.net/wow/recipe/33994?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    # SPELL
    @responses.activate
    def test_get_spell(self):
        """get_spell sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_spell(TEST_WOW_SPELL_ID)

        expected_url = 'https://us.api.battle.net/wow/spell/8056?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    # ZONE
    @responses.activate
    def test_get_zones(self):
        """get_zones sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_zones()

        expected_url = 'https://us.api.battle.net/wow/zone/?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url


    @responses.activate
    def test_get_zone(self):
        """get_zone sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_zone(TEST_WOW_ZONE_ID)

        expected_url = 'https://us.api.battle.net/wow/zone/4131?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    # DATA RESOURCES
    @responses.activate
    def test_get_data_battlegroups(self):
        """get_data_battlegroups sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_data_battlegroups()

        expected_url = 'https://us.api.battle.net/wow/data/battlegroups/?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_data_character_races(self):
        """get_data_character_races sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_data_character_races()

        expected_url = 'https://us.api.battle.net/wow/data/character/races?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_data_character_classes(self):
        """get_data_character_classes sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_data_character_classes()

        expected_url = 'https://us.api.battle.net/wow/data/character/classes?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_data_character_achievements(self):
        """get_data_character_achievements sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_data_character_achievements()

        expected_url = 'https://us.api.battle.net/wow/data/character/achievements?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_data_guild_rewards(self):
        """get_data_guild_rewards sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_data_guild_rewards()

        expected_url = 'https://us.api.battle.net/wow/data/guild/rewards?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_data_guild_perks(self):
        """get_data_guild_perks sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_data_guild_perks()

        expected_url = 'https://us.api.battle.net/wow/data/guild/perks?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_data_guild_achievements(self):
        """get_data_guild_achievements sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_data_guild_achievements()

        expected_url = 'https://us.api.battle.net/wow/data/guild/achievements?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_data_item_classes(self):
        """get_data_item_classes sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_data_item_classes()

        expected_url = 'https://us.api.battle.net/wow/data/item/classes?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_data_talents(self):
        """get_data_talents sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_data_talents()

        expected_url = 'https://us.api.battle.net/wow/data/talents?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_data_pet_types(self):
        """get_data_pet_types sends a request with the expected URL."""
        wow = self.create_test_world_of_warcraft_instance()
        wow.get_data_pet_types()

        expected_url = 'https://us.api.battle.net/wow/data/pet/types?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url