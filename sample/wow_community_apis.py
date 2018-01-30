from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.common.utility import util
from pyblizzard.pyblizzard import PyBlizzard
from pyblizzard.wow.enum.characterprofilefield import CharacterProfileField
from pyblizzard.wow.pvpbracket import PvpBracket
from sample.config import testconfig

SAMPLE_WOW_ACHIEVEMENT_ID = '2144'
SAMPLE_WOW_GUILD_NAME = 'Basement Dwellers'
SAMPLE_WOW_REALM = 'Emerald Dream'
SAMPLE_WOW_CHARACTER_NAME = 'Spittles'
SAMPLE_WOW_BOSS_ID = '24723'
SAMPLE_WOW_ITEM_ID = '18803'
SAMPLE_WOW_ITEM_SET_ID = '1060'
SAMPLE_WOW_PET_ABILITY_ID = '640'
SAMPLE_WOW_PET_SPECIES_ID = '258'
SAMPLE_WOW_QUEST_ID = '13146'
SAMPLE_WOW_RECIPE_ID = '33994'
SAMPLE_WOW_SPELL_ID = '234302'
SAMPLE_WOW_ZONE_ID = '4131'


def main():
    sample_api_key = testconfig.get_api_key()

    py_blizzard = PyBlizzard(sample_api_key, Region.US.value, Locale.US.value)

    # ACHIEVEMENT
    print('Getting achievement....')
    achievement = py_blizzard.wow.get_achievement(SAMPLE_WOW_ACHIEVEMENT_ID)
    util.print_response_object(achievement)

    # AUCTION DATA
    print('Getting auction data....')
    auction_data = py_blizzard.wow.get_auction_data(SAMPLE_WOW_REALM)
    util.print_response_object(auction_data)

    # BOSS
    print('Getting bosses....')
    bosses = py_blizzard.wow.get_bosses()
    util.print_response_object(bosses)

    print('Getting boss...')
    boss = py_blizzard.wow.get_boss(SAMPLE_WOW_BOSS_ID)
    util.print_response_object(boss)

    # CHALLENGE
    print('Getting challenge leaderboard for realm...')
    realm_challenge_leaderboard = py_blizzard.wow.get_realm_challenge_leaderboard(SAMPLE_WOW_REALM)
    util.print_response_object(realm_challenge_leaderboard)

    print('Getting challenge leaderboard for region...')
    region_challenge_leaderboard = py_blizzard.wow.get_region_challenge_leaderboard()
    util.print_response_object(region_challenge_leaderboard)

    # CHARACTER PROFILE
    print('Getting character profile...')
    character_profile = py_blizzard.wow.get_character_profile(SAMPLE_WOW_REALM, SAMPLE_WOW_CHARACTER_NAME, CharacterProfileField.TALENTS, CharacterProfileField.ITEMS)
    util.print_response_object(character_profile)

    # GUILD PROFILE
    print('Getting guild profile...')
    guild_profile = py_blizzard.wow.get_guild_profile(SAMPLE_WOW_REALM, SAMPLE_WOW_GUILD_NAME)
    util.print_response_object(guild_profile)

    # ITEM
    print('Getting item...')
    item = py_blizzard.wow.get_item(SAMPLE_WOW_ITEM_ID)
    util.print_response_object(item)

    print('Getting item set...')
    item_set = py_blizzard.wow.get_item_set(SAMPLE_WOW_ITEM_SET_ID)
    util.print_response_object(item_set)

    # MOUNT
    try:
        print('Getting mounts...')
        mounts = py_blizzard.wow.get_mounts()
        util.print_response_object(mounts)
    except Exception as e:
        print(e)

    # PET
    print('Getting pets...')
    pets = py_blizzard.wow.get_pets()
    util.print_response_object(pets)

    print('Getting pet ability...')
    pet_ability = py_blizzard.wow.get_pet_ability(SAMPLE_WOW_PET_ABILITY_ID)
    util.print_response_object(pet_ability)

    print('Getting pet species...')
    pet_species = py_blizzard.wow.get_pet_species(SAMPLE_WOW_PET_SPECIES_ID)
    util.print_response_object(pet_species)

    print('Getting pet stats...')
    pet_stats = py_blizzard.wow.get_pet_stats_by_species(SAMPLE_WOW_PET_SPECIES_ID)
    util.print_response_object(pet_stats)

    # PVP
    print('Getting PVP leaderboard...')
    pvp_leaderboard = py_blizzard.wow.get_pvp_leaderboard_for_bracket(PvpBracket.two_v_two)
    util.print_response_object(pvp_leaderboard)

    # QUEST
    print('Getting quest...')
    quest = py_blizzard.wow.get_quest(SAMPLE_WOW_QUEST_ID)
    util.print_response_object(quest)

    # REALM STATUS
    print('Getting realm status...')
    realm_status = py_blizzard.wow.get_realm_status(['aegwynn', 'aerie-peak'])
    util.print_response_object(realm_status)

    # RECIPE
    print('Getting recipe...')
    recipe = py_blizzard.wow.get_recipe(SAMPLE_WOW_RECIPE_ID)
    util.print_response_object(recipe)

    # SPELL
    print('Getting spell...')
    spell = py_blizzard.wow.get_spell(SAMPLE_WOW_SPELL_ID)
    util.print_response_object(spell)

    # ZONE
    print('Getting zones...')
    zones = py_blizzard.wow.get_zones()
    util.print_response_object(zones)

    print('Getting zone...')
    zone = py_blizzard.wow.get_zone(SAMPLE_WOW_ZONE_ID)
    util.print_response_object(zone)

    # DATA RESOURCES
    print('Getting battlegroups...')
    battlegroups = py_blizzard.wow.get_data_battlegroups()
    util.print_response_object(battlegroups)

    print('Getting character races...')
    character_races = py_blizzard.wow.get_data_character_races()
    util.print_response_object(character_races)

    print('Getting character classes...')
    character_classes = py_blizzard.wow.get_data_character_classes()
    util.print_response_object(character_classes)

    print('Getting character achievements...')
    character_achievements = py_blizzard.wow.get_data_character_achievements()
    util.print_response_object(character_achievements)

    print('Getting guild rewards...')
    guild_rewards = py_blizzard.wow.get_data_guild_rewards()
    util.print_response_object(guild_rewards)

    print('Getting guild perks...')
    guild_perks = py_blizzard.wow.get_data_guild_perks()
    util.print_response_object(guild_perks)

    print('Getting guild achievements...')
    guild_achievements = py_blizzard.wow.get_data_guild_achievements()
    util.print_response_object(guild_achievements)

    print('Getting item classes...')
    item_classes = py_blizzard.wow.get_data_item_classes()
    util.print_response_object(item_classes)

    print('Getting talents...')
    talents = py_blizzard.wow.get_data_talents()
    util.print_response_object(talents)

    print('Getting pet types...')
    pet_types = py_blizzard.wow.get_data_pet_types()
    util.print_response_object(pet_types)


if __name__ == '__main__':
    main()