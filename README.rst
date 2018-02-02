.. image:: https://i.imgur.com/jP6WNHR.png

.. image:: https://travis-ci.org/scb5304/pyblizzard.svg?branch=master
    :target: https://travis-ci.org/scb5304/pyblizzard
    
.. image:: https://api.codacy.com/project/badge/Grade/43a42087f55f4fd0a75b9a20381ab302    
    :target: https://www.codacy.com/app/scb5304/pyblizzard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=scb5304/pyblizzard&amp;utm_campaign=Badge_Grade
    
.. image:: https://api.codacy.com/project/badge/Coverage/43a42087f55f4fd0a75b9a20381ab302    
    :target: https://www.codacy.com/app/scb5304/pyblizzard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=scb5304/pyblizzard&amp;utm_campaign=Badge_Coverage

About
---------------
pyblizzard is a simple, object-oriented `Battle.net API <https://dev.battle.net/io-docs>`_ wrapper written in Python that covers a majority of the Community APIs (the China-specific Community APIs not yet covered). Each  `request <https://github.com/requests/requests>`_  returns a Python object created from the JSON response using `jsonpickle <https://jsonpickle.github.io/>`_.

Installation
---------------

.. code-block:: python

  >>> pip install pyblizzard


Usage
---------------

.. code-block:: python

  >>> py_blizzard = PyBlizzard('apikey', Region.US, Locale.US) 
  
  >>> wow_quest = py_blizzard.wow.get_quest('13146') 
  >>> wow_quest
  {'category': 'Icecrown', 'id': 13146, 'level': 80, 'reqLevel': 77, 'suggestedPartyMembers': 0, 'title': 'Generosity Abounds'}
  
  >>> match_history = py_blizzard.starcraft2.get_profile_match_history('2137104', 'skt') 
  >>> match_history
  {"matches": [{"date": 1425172458, "decision": "BAILER", "map": "Airstrike", "speed": "FASTER", "type": "CUSTOM"}, {"date": 1362927359, "decision": "WIN", "map": "Daybreak LE", "speed": "FASTER", "type": "CUSTOM"}, ... ]} 

  >>> diablo_item = py_blizzard.diablo.get_item_data('Unique_CombatStaff_2H_001_x1')
  >>> diablo_item
  {'accountBound': True, 'attacksPerSecond': {'max': 1.100000023841858, 'min': 1.100000023841858}, 'attacksPerSecondText': '1.10 Attacks per Second', 'attributes': {'passive': [], 'primary': [{'affixType': 'default', 'color': 'blue', 'text': '+495–787 Dexterity'} ...


Some endpoints support a variable number of arguments to limit data returned. If you do not specify any, then all are included. Below, the character profile includes common information about gender, level, name, etc, but full objects for 'achievements' and 'feed' due to these arguments being passed.

.. code-block:: python

  >>> wow_character_profile = py_blizzard.wow.get_character_profile('emerald-dream', 'Spittles', CharacterProfileField.ACHIEVEMENTS, CharacterProfileField.FEED)
  >>> wow_character_profile
  {'achievementPoints': 4815, 'achievements': {'achievementsCompleted': [6, ..., 1473639952000]}, 'battlegroup': 'Shadowburn', 'calcClass': 'e', 'class': 8, 'faction': 0, 'feed': [{'achievement': {'accountWide': False, 'criteria': [{'description': '', 'id': 31379, 'max': 1, 'orderIndex': 0}], 'description': 'Defeat the Wrath of Azshara in Eye of Azshara.', 'factionId': 2, 'icon': 'achievement_dungeon_eyeofazshara', 'id': 10780, 'points': 10, 'rewardItems': [], 'title': 'Eye of Azshara'}, 'featOfStrength': False, 'timestamp': 1473643020000, 'type': 'ACHIEVEMENT'} ... ], 'gender': 1, 'lastModified': 1457118698000, 'level': 100, 'name': 'Spittles', 'race': 1, 'realm': 'Emerald Dream', 'thumbnail': 'emerald-dream/140/143613580-avatar.jpg', 'totalHonorableKills': 814}

Check out the `samples <https://github.com/scb5304/pyblizzard/tree/master/samples>`_  directory for examples of how to communicate with every API and endpoint.
