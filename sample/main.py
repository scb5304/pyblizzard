import logging
import sys
import traceback
import jsonpickle

from pyblizzard.wow.enum.characterprofilefield import CharacterProfileField
from pyblizzard.wow.pvpbracket import PvpBracket

logging.basicConfig(level=logging.DEBUG)

from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.diablo.enum.artisan import Artisan
from pyblizzard.diablo.enum.follower import Follower
from pyblizzard.pyblizzard import PyBlizzard
from sample.config import testconfig

SAMPLE_DIABLO_BATTLE_TAG = 'Spittles-1502'
SAMPLE_DIABLO_HERO_ID = '94825371'
SAMPLE_DIABLO_ITEM_ID = 'Unique_CombatStaff_2H_001_x1'

SAMPLE_STARCRAFT2_PROFILE_ID = '2137104'
SAMPLE_STARCRAFT2_PROFILE_NAME = 'skt'
SAMPLE_STARCRAFT2_LADDER_ID = '194163'

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
SAMPLE_WOW_SPELL_ID = '8056'
SAMPLE_WOW_ZONE_ID = '4131'

def print_result(response_object):
    print(jsonpickle.encode(response_object, unpicklable=False))

def main():
    sample_api_key = None
    try:
        sample_api_key = testconfig.get_api_key()
    except KeyError:
        print('There was an error reading in test\'s config file')
        print(traceback.format_exc())

    if not sample_api_key:
        print('Cannot proceed without an API key.')
        sys.exit(1)

    py_blizzard = PyBlizzard(sample_api_key, Region.US.value, Locale.US.value)

    #  --- DIABLO ---
    career_profile = py_blizzard.diablo.get_career_profile(SAMPLE_DIABLO_BATTLE_TAG)
    print_result(career_profile)

    hero_profile = py_blizzard.diablo.get_hero_profile(SAMPLE_DIABLO_BATTLE_TAG, SAMPLE_DIABLO_HERO_ID)
    print_result(hero_profile)

    item = py_blizzard.diablo.get_item_data(SAMPLE_DIABLO_ITEM_ID)
    print_result(item)

    follower = py_blizzard.diablo.get_follower_data(Follower.ENCHANTRESS.value)
    print_result(follower)

    artisan = py_blizzard.diablo.get_artisan_data(Artisan.MYSTIC.value)
    print_result(artisan)

    #  --- STARCRAFT2  ---
    profile = py_blizzard.starcraft2.get_profile(SAMPLE_STARCRAFT2_PROFILE_ID, SAMPLE_STARCRAFT2_PROFILE_NAME)
    print_result(profile)

    ladders = py_blizzard.starcraft2.get_profile_ladders(SAMPLE_STARCRAFT2_PROFILE_ID, SAMPLE_STARCRAFT2_PROFILE_NAME)
    print_result(ladders)

    match_history = py_blizzard.starcraft2.get_profile_match_history(SAMPLE_STARCRAFT2_PROFILE_ID, SAMPLE_STARCRAFT2_PROFILE_NAME)
    print_result(match_history)

    ladder = py_blizzard.starcraft2.get_ladder(SAMPLE_STARCRAFT2_LADDER_ID)
    print_result(ladder)

    achievements = py_blizzard.starcraft2.get_achievements_data()
    print_result(achievements)

    rewards = py_blizzard.starcraft2.get_rewards_data()
    print_result(rewards)

    # --- WORLD OF WARCRAFT ---

    # ACHIEVEMENT
    achievement = py_blizzard.wow.get_achievement(SAMPLE_WOW_ACHIEVEMENT_ID)
    print_result(achievement)

    # AUCTION DATA
    auction_data = py_blizzard.wow.get_auction_data(SAMPLE_WOW_REALM)
    print_result(auction_data)

    # BOSS
    bosses = py_blizzard.wow.get_bosses()
    print_result(bosses)

    boss = py_blizzard.wow.get_boss(SAMPLE_WOW_BOSS_ID)
    print_result(boss)

    # CHALLENGE
    realm_challenge_leaderboard = py_blizzard.wow.get_realm_challenge_leaderboard(SAMPLE_WOW_REALM)
    print(realm_challenge_leaderboard)

    region_challenge_leaderboard = py_blizzard.wow.get_region_challenge_leaderboard()
    print(region_challenge_leaderboard)

    # CHARACTER PROFILE
    character_profile = py_blizzard.wow.get_character_profile(SAMPLE_WOW_REALM, SAMPLE_WOW_CHARACTER_NAME,
                                                              CharacterProfileField.ACHIEVEMENTS,
                                                              CharacterProfileField.HUNTER_PETS,
                                                              CharacterProfileField.PVP)
    print_result(character_profile)

    # GUILD PROFILE
    guild_profile = py_blizzard.wow.get_guild_profile(SAMPLE_WOW_REALM, SAMPLE_WOW_GUILD_NAME)
    print_result(guild_profile)

    # ITEM
    item = py_blizzard.wow.get_item(SAMPLE_WOW_ITEM_ID)
    print_result(item)

    item_set = py_blizzard.wow.get_item_set(SAMPLE_WOW_ITEM_SET_ID)
    print_result(item_set)

    # MOUNT
    mounts = py_blizzard.wow.get_mounts()
    print_result(mounts)

    # PET
    pets = py_blizzard.wow.get_pets()
    print_result(pets)

    pet_ability = py_blizzard.wow.get_pet_ability(SAMPLE_WOW_PET_ABILITY_ID)
    print_result(pet_ability)

    pet_species = py_blizzard.wow.get_pet_species(SAMPLE_WOW_PET_SPECIES_ID)
    print_result(pet_species)

    pet_stats = py_blizzard.wow.get_pet_stats_by_species(SAMPLE_WOW_PET_SPECIES_ID)
    print_result(pet_stats)

    # PVP
    pvp_leaderboard = py_blizzard.wow.get_pvp_leaderboard_for_bracket(PvpBracket.two_v_two)
    print_result(pvp_leaderboard)

    # QUEST
    quest = py_blizzard.wow.get_quest(SAMPLE_WOW_QUEST_ID)
    print_result(quest)

    # REALM STATUS
    realm_status = py_blizzard.wow.get_realm_status(['aegwynn', 'aerie-peak'])
    print_result(realm_status)

    # RECIPE
    recipe = py_blizzard.wow.get_recipe(SAMPLE_WOW_RECIPE_ID)
    print_result(recipe)

    # SPELL
    spell = py_blizzard.wow.get_spell(SAMPLE_WOW_SPELL_ID)
    print_result(spell)

    # ZONE
    zones = py_blizzard.wow.get_zones()
    print_result(zones)

    zone = py_blizzard.wow.get_zone(SAMPLE_WOW_ZONE_ID)
    print_result(zone)

    # DATA RESOURCES
    battlegroups = py_blizzard.wow.get_data_battlegroups()
    print_result(battlegroups)

    character_races = py_blizzard.wow.get_data_character_races()
    print_result(character_races)

    character_classes = py_blizzard.wow.get_data_character_classes()
    print_result(character_classes)

    character_achievements = py_blizzard.wow.get_data_character_achievements()
    print_result(character_achievements)

    guild_rewards = py_blizzard.wow.get_data_guild_rewards()
    print_result(guild_rewards)

    guild_perks = py_blizzard.wow.get_data_guild_perks()
    print_result(guild_perks)

    guild_achievements = py_blizzard.wow.get_data_guild_achievements()
    print_result(guild_achievements)

    item_classes = py_blizzard.wow.get_data_item_classes()
    print_result(item_classes)

    talents = py_blizzard.wow.get_data_talents()
    print_result(talents)

    pet_types = py_blizzard.wow.get_data_pet_types()
    print_result(pet_types)


if __name__ == '__main__':
    main()
