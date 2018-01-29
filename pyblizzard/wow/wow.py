import jsonpickle
import requests

from pyblizzard import pyblizzard
from pyblizzard.common.utility import util
from pyblizzard.common.utility.urlbuilder import UrlBuilder as UrlBuilder
from pyblizzard.wow.enum.characterprofilefield import CharacterProfileField
from pyblizzard.wow.enum.guildprofilefield import GuildProfileField
from pyblizzard.wow.pvpbracket import PvpBracket

GAME_NAME = 'wow'

ENDPOINT_ACHIEVEMENT = 'achievement'
ENDPOINT_AUCTION = 'auction'
ENDPOINT_BOSS = 'boss'
ENDPOINT_CHALLENGE = 'challenge'
ENDPOINT_CHARACTER_PROFILE = 'character'
ENDPOINT_GUILD_PROFILE = 'guild'
ENDPOINT_ITEM = 'item'
ENDPOINT_MOUNT = 'mount'
ENDPOINT_PET = 'pet'
ENDPOINT_PVP = 'leaderboard'
ENDPOINT_QUEST = 'quest'
ENDPOINT_REALM_STATUS = 'realm'
ENDPOINT_RECIPE = 'recipe'
ENDPOINT_SPELL = 'spell'
ENDPOINT_ZONE = 'zone'
ENDPOINT_DATA_RESOURCES = 'data'

QUERY_FIELDS = 'fields'

class WorldOfWarcraft:
    def build_wow_path(self):
        base_blizzard_path = util.build_base_path_from_region(self._region)
        return UrlBuilder() \
            .add(base_blizzard_path) \
            .add(GAME_NAME) \
            .build()

    def init_params(self):
        self._params = {pyblizzard.QUERY_LOCALE: self._locale, pyblizzard.QUERY_API_KEY: self._api_key}

    def __init__(self, api_key, region, locale, timeout):
        self._api_key = api_key
        self._region = region
        self._locale = locale
        self._timeout = timeout
        self._base_wow_path = self.build_wow_path()
        self._params = None
        self.init_params()

    def set_timeout(self, timeout):
        self._timeout = timeout

    def _get_wow_generic(self, path):
        full_path = UrlBuilder() \
            .add(self._base_wow_path) \
            .add(path) \
            .build()
        response = requests.get(full_path, params=self._params, timeout=self._timeout)
        self.init_params()
        return jsonpickle.decode(response.text)

    # ACHIEVEMENT API
    def get_achievement(self, achievement_id):
        achievement_path = UrlBuilder() \
            .add(ENDPOINT_ACHIEVEMENT) \
            .add(achievement_id) \
            .build()
        return self._get_wow_generic(achievement_path)

    # AUCTION API
    def get_auction_data(self, realm):
        """Checks if there is a recent auction house data dump for this realm. If so, it returns the most recent one.
        THIS MAY TAKE A VERY LONG TIME DEPENDING ON THE AMOUNT OF DATA STORED."""
        auction_path = UrlBuilder() \
            .add(ENDPOINT_AUCTION) \
            .add('data') \
            .add(realm) \
            .build()
        auction_initial_result = self._get_wow_generic(auction_path)
        print(auction_initial_result)
        auction_initial_result_files = auction_initial_result['files']

        if auction_initial_result_files and len(auction_initial_result_files) > 0:
            auction_result_two = requests.get(auction_initial_result_files[0]['url'])
            return jsonpickle.decode(auction_result_two.text)
        else:
            return {}

    # BOSS API
    def get_bosses(self):
        bosses_path = UrlBuilder(use_trailing_slash=True) \
            .add(ENDPOINT_BOSS) \
            .build()
        return self._get_wow_generic(bosses_path)

    def get_boss(self, boss_id):
        boss_path = UrlBuilder() \
            .add(ENDPOINT_BOSS) \
            .add(boss_id) \
            .build()
        return self._get_wow_generic(boss_path)

    # CHALLENGE MODE API
    def get_realm_challenge_leaderboard(self, realm):
        realm_leaderboard_path = UrlBuilder() \
            .add(ENDPOINT_CHALLENGE) \
            .add(realm) \
            .build()
        return self._get_wow_generic(realm_leaderboard_path)

    def get_region_challenge_leaderboard(self):
        realm_leaderboard_path = UrlBuilder() \
            .add(ENDPOINT_CHALLENGE) \
            .add('region') \
            .build()
        return self._get_wow_generic(realm_leaderboard_path)

    # CHARACTER PROFILE API
    def get_character_profile(self, realm, character_name, *args):
        if not args:
            fields = util.get_delimited_enum_value_str(list(CharacterProfileField), ' ')
        else:
            fields = util.get_delimited_enum_value_str(args, ' ')
        self._params['fields'] = fields
        character_profile_path = UrlBuilder() \
            .add(ENDPOINT_CHARACTER_PROFILE) \
            .add(realm) \
            .add(character_name) \
            .build()
        return self._get_wow_generic(character_profile_path)

    # GUILD PROFILE API
    def get_guild_profile(self, realm, guild_name, *args):
        if not args:
            fields = util.get_delimited_enum_value_str(list(GuildProfileField), ' ')
        else:
            fields = util.get_delimited_enum_value_str(args, ' ')
        self._params['fields'] = fields
        guild_profile_path = UrlBuilder() \
            .add(ENDPOINT_GUILD_PROFILE) \
            .add(realm) \
            .add(guild_name) \
            .build()
        return self._get_wow_generic(guild_profile_path)

    # ITEM API
    def get_item(self, item_id):
        item_path = UrlBuilder() \
            .add(ENDPOINT_ITEM) \
            .add(item_id) \
            .build()
        return self._get_wow_generic(item_path)

    def get_item_set(self, item_set_id):
        item_path = UrlBuilder() \
            .add(ENDPOINT_ITEM) \
            .add('set') \
            .add(item_set_id) \
            .build()
        return self._get_wow_generic(item_path)

    # MOUNT API
    def get_mounts(self):
        mounts_path = UrlBuilder(use_trailing_slash=True) \
            .add(ENDPOINT_MOUNT) \
            .build()
        return self._get_wow_generic(mounts_path)

    # PET API
    def get_pets(self):
        pets_path = UrlBuilder() \
            .add(ENDPOINT_PET) \
            .build()
        return self._get_wow_generic(pets_path)

    def get_pet_ability(self, pet_ability_id):
        pet_ability_path = UrlBuilder() \
            .add(ENDPOINT_PET) \
            .add('ability') \
            .add(pet_ability_id) \
            .build()
        return self._get_wow_generic(pet_ability_path)

    def get_pet_species(self, pet_species_id):
        pet_species_path = UrlBuilder() \
            .add(ENDPOINT_PET) \
            .add('species') \
            .add(pet_species_id) \
            .build()
        return self._get_wow_generic(pet_species_path)

    def get_pet_stats_by_species(self, pet_species_id):
        pet_species_path = UrlBuilder() \
            .add(ENDPOINT_PET) \
            .add('stats') \
            .add(pet_species_id) \
            .build()
        return self._get_wow_generic(pet_species_path)

    # PVP API
    def get_pvp_leaderboard_for_bracket(self, pvp_bracket):
        if not isinstance(pvp_bracket, PvpBracket):
            print('Must be an instance of PvpBracket!')
            return
        else:
            pvp_leaderboard_path = UrlBuilder() \
                .add(ENDPOINT_PVP) \
                .add(pvp_bracket.value) \
                .build()
            return self._get_wow_generic(pvp_leaderboard_path)

    # QUEST API
    def get_quest(self, quest_id):
        quest_path = UrlBuilder() \
            .add(ENDPOINT_QUEST) \
            .add(quest_id) \
            .build()
        return self._get_wow_generic(quest_path)

    # REALM STATUS API
    def get_realm_status(self, limit_to_realms=None):
        if limit_to_realms:
            self._params['realms'] = ' '.join(limit_to_realms)
        realms_path = UrlBuilder() \
            .add(ENDPOINT_REALM_STATUS) \
            .add('status') \
            .build()
        return self._get_wow_generic(realms_path)

    # RECIPE API
    def get_recipe(self, recipe_id):
        recipe_path = UrlBuilder() \
            .add(ENDPOINT_RECIPE) \
            .add(recipe_id) \
            .build()
        return self._get_wow_generic(recipe_path)

    # SPELL API
    def get_spell(self, spell_id):
        spell_path = UrlBuilder() \
            .add(ENDPOINT_SPELL) \
            .add(spell_id) \
            .build()
        return self._get_wow_generic(spell_path)

    # ZONE API
    def get_zones(self):
        zones_path = UrlBuilder(use_trailing_slash=True) \
            .add(ENDPOINT_ZONE) \
            .build()
        return self._get_wow_generic(zones_path)

    def get_zone(self, zone_id):
        zone_path = UrlBuilder() \
            .add(ENDPOINT_ZONE) \
            .add(zone_id) \
            .build()
        return self._get_wow_generic(zone_path)

    # DATA RESOURCES API
    def get_data_battlegroups(self):
        battlegroups_path = UrlBuilder(use_trailing_slash=True) \
            .add(ENDPOINT_DATA_RESOURCES) \
            .add('battlegroups') \
            .build()
        return self._get_wow_generic(battlegroups_path)

    def get_data_character_races(self):
        character_races_path = UrlBuilder() \
            .add(ENDPOINT_DATA_RESOURCES) \
            .add('character') \
            .add('races') \
            .build()
        return self._get_wow_generic(character_races_path)

    def get_data_character_classes(self):
        character_classes_path = UrlBuilder() \
            .add(ENDPOINT_DATA_RESOURCES) \
            .add('character') \
            .add('classes') \
            .build()
        return self._get_wow_generic(character_classes_path)

    def get_data_character_achievements(self):
        character_achievements_path = UrlBuilder() \
            .add(ENDPOINT_DATA_RESOURCES) \
            .add('character') \
            .add('achievements') \
            .build()
        return self._get_wow_generic(character_achievements_path)

    def get_data_guild_rewards(self):
        guild_rewards_path = UrlBuilder() \
            .add(ENDPOINT_DATA_RESOURCES) \
            .add('guild') \
            .add('rewards') \
            .build()
        return self._get_wow_generic(guild_rewards_path)

    def get_data_guild_perks(self):
        guild_perks_path = UrlBuilder() \
            .add(ENDPOINT_DATA_RESOURCES) \
            .add('guild') \
            .add('perks') \
            .build()
        return self._get_wow_generic(guild_perks_path)

    def get_data_guild_achievements(self):
        guild_perks_path = UrlBuilder() \
            .add(ENDPOINT_DATA_RESOURCES) \
            .add('guild') \
            .add('achievements') \
            .build()
        return self._get_wow_generic(guild_perks_path)

    def get_data_item_classes(self):
        item_classes_path = UrlBuilder() \
            .add(ENDPOINT_DATA_RESOURCES) \
            .add('item') \
            .add('classes') \
            .build()
        return self._get_wow_generic(item_classes_path)

    def get_data_talents(self):
        talents_path = UrlBuilder() \
            .add(ENDPOINT_DATA_RESOURCES) \
            .add('talents') \
            .build()
        return self._get_wow_generic(talents_path)

    def get_data_pet_types(self):
        pet_types_path = UrlBuilder() \
            .add(ENDPOINT_DATA_RESOURCES) \
            .add('pet') \
            .add('types') \
            .build()
        return self._get_wow_generic(pet_types_path)