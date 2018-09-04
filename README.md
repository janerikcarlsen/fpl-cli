[![Build Status](https://travis-ci.org/janerikcarlsen/fpl-cli.svg?branch=master)](https://travis-ci.org/janerikcarlsen/fpl-cli)
[![Python Versions](https://img.shields.io/pypi/pyversions/fplcli.svg)](https://pypi.org/project/fplcli)

# fpl-cli
fpl-cli is a command line tool for Fantasy Premier League, written in Python.
The tool gets its data from the official Fantasy Premier League API, and currently supports the following actions:  
```
fpl                     Returns help menu
fpl configure           Set up team_id (required)
fpl points              Returns live points for a team
fpl leagues             Returns all leagues for a team entry
fpl league <id>         Returns confirmed scores for a league by id
fpl liveleague <id>     Returns live scores for a league by id
fpl entry               Returns information about a team entry
fpl players             Returns all players in the game, sorted by total score
```

# Installing 
fpl-cli has been tested with Python versions 2.7, 3.4, 3.5, 3.6 and 3.7.
In a terminal window, verify that Python and pip is available: 
```
python --version
pip --version
``` 
If no Python/pip version is found, [download Python and pip before proceeding](https://www.python.org/downloads/)
```
pip install fplcli
```

# Using fpl-cli
## Configure fpl-cli 
Start using fpl-cli by telling it your team_id. You can find your team_id by going to the Points tab at https://fantasy.premierleague.com and find the number in between `team/` and `event/` in the url.

![fpl configure](docs/img/fpl_configure.png?raw=true "fpl configure")

## Get help 
Get an overview of the allowed actions by typing `fpl` or `fpl --help`

![fpl help](docs/img/fpl_help.png?raw=true "fpl help")

## Get current points total for team
The points total and player score is updated during games based on live score data. Provisional bonus are not included yet.

![fpl points](docs/img/fpl_points.png?raw=true "fpl points")

## Get all leagues the team is member of
Returns all leagues you participate in (Head 2 Head leagues not included yet)

![fpl leagues](docs/img/fpl_leagues.png?raw=true "fpl leagues")

## Get league standings
Returns league standings for a single league. You find the league_id in the leftmost `Id` column in the `fpl leagues` result

![fpl league](docs/img/fpl_league.png?raw=true "fpl league")

## Get live league standings
Returns live league standings for a single league, where all teams score are updated in real time based on live score data. This one is a separate action from the `fpl league` action because it requires ~2 API calls for each team in the league and is therefore slower (~1-10 seconds depending on league size and response times from Fantasy Premier League API).

![fpl liveleague](docs/img/fpl_liveleague.png?raw=true "fpl liveleague")


# Planned features
Planned future features include:

* Include all major features from fantasy.premierleague.com
* Include H2H leagues in leagues view
* Actions that require authentication with the FPL API (Making transfers, prepare team for next Gameweek)
* Live updates of league standings during games based on new points total
* Include provisional bonus in live league and points view
* Player sorting/filtering and enriched player staticstics
* Cache API calls to improve response times, especially for live leagues
* Transfer suggestions based on form and upcoming fixture difficulty

Ideas for features or enhancements that you would like to see from fpl-cli are welcome, please post an [issue in the GitHub repository](https://github.com/janerikcarlsen/fpl-cli/issues), or even better, submit a Pull Request with the suggested change.

# Develop
To develop fpl-cli: 
* Clone this repository
* Create a virtualenv using python 2.7, 3.4, 3.5, 3.6 or 3.7, and inside that: 
* `pip install -r requirements.txt`
* `pip install -r ci-requirements.txt`