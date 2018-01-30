# pyblizzard

<div>
  <p>
    <img src="https://i.imgur.com/jP6WNHR.png" />
  </p>
</div>

[![Build Status](https://travis-ci.org/scb5304/pyblizzard.svg?branch=master)](https://travis-ci.org/scb5304/pyblizzard)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/43a42087f55f4fd0a75b9a20381ab302)](https://www.codacy.com/app/scb5304/pyblizzard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=scb5304/pyblizzard&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/43a42087f55f4fd0a75b9a20381ab302)](https://www.codacy.com/app/scb5304/pyblizzard?utm_source=github.com&utm_medium=referral&utm_content=scb5304/pyblizzard&utm_campaign=Badge_Coverage)

## About
pyblizzard is a simple, object-oriented [Battle.net API](https://dev.battle.net/io-docs) wrapper in Python with 100% coverage of the Community APIs. Each request returns a Python object created from the JSON response using [jsonpickle](https://jsonpickle.github.io/).

## Installation
...probably something like this if I figure out how that all works.
```
pip install pyblizzard
```


## Usage

1. Create a PyBlizzard instance.

```
py_blizzard = PyBlizzard(<api_key>, Region.US, Locale.US)
```

2. Make a call to one of the community APIs.

```
wow_quest = py_blizzard.wow.get_quest('13146')
starcraft_ladder = py_blizzard.starcraft2.get_ladder('194163')
diablo_hero_profile = py_blizzard.diablo.get_hero_profile(<battle_tag>, <hero_id>)
```

- Some endpoints support a variable number of arguments to limit data returned, as documented in the [Battle.net API](https://dev.battle.net/io-docs). The returned objects will only include these data fields. If none are specified, then all are included.

```
wow_character_profile = py_blizzard.wow.get_character_profile(<realm>, <char_name>, CharacterProfileField.ACHIEVEMENTS, CharacterProfileField.FEED)
wow_guild_profile = py_blizzard.wow.get_guild_profile(<realm>, <guild_name>, GuildProfileField.ACHIEVEMENTS, GuildProfileField.NEWS, GuildProfileField.CHALLENGE)
```

Check out the [sample](https://github.com/scb5304/pyblizzard/tree/master/sample) directory for examples of how to communicate with every API and endpoint.

