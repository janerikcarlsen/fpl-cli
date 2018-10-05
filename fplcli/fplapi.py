import os
import sys
import configparser
import requests

from .classic_league_standings import ClassicLeagueStandings
from .element_type import ElementType
from .entry import Entry
from .fixture import Fixture
from .gameweek import Gameweek
from .league import LeagueEntry
from .league import LeagueStandings
from .league import LiveLeagueStandings
from .player import Player
from .picks import Picks
from .element_stats import ElementStats
from .urls import FPL_URL
from .urls import LIVE_SUBURL
from .urls import PICKS_SUBURL
from .urls import LOGIN_BASE_URL
from .urls import LOGIN_SUBURL
from .urls import LEAGUE_H2H_STANDING_SUBURL
from .urls import BOOTSTRAP
from .urls import PLAYERS_INFO_SUBURL
from .urls import BOOTSTRAP_DYNAMIC_URL
from .urls import GAMEWEEK_URL
from .urls import GAMEWEEKS_URL
from .urls import ELEMENT_TYPES_URL
from .urls import FIXTURES_SUBURL
from .urls import REGION_URL
from .urls import TRANSFERS_URL
from .urls import ENTRY_BY_ID_URL
from .urls import ENTRY_HISTORY_SUBURL
from .urls import ENTRIES_URL
from .urls import MY_TEAM_URL
from .urls import LEAGUES_ENTERED_URL
from .urls import LEAGUES_CLASSIC_URL
from .urls import LEAGUES_CLASSIC_STANDINGS_URL

def players(): # OK
    """Return all players, sorted by total points"""
    players = []
    for p in get_url(PLAYERS_INFO_SUBURL):
        players.append(Player(p))
    players.sort(key=lambda player: player.total_points, reverse=True)
    return players

def get_current_gameweek_id():
    """Return the id of the current Gameweek"""
    gameweeks = get_url(GAMEWEEKS_URL)
    for gw in gameweeks: 
        if gw["is_current"]: 
            return gw["id"]
    raise Exception("No current gameweek found")

def leagues_entered(team_id): # OK
    """Return the leagues entered for the current team_id"""
    entry = Entry(get_url(ENTRY_BY_ID_URL, item_id=team_id))
    return entry.leagues


def league(league_id): # Add H2H and global leagues, check for behaviour
    """Return a league by league_id"""
    return LeagueStandings(get_url(LEAGUES_CLASSIC_STANDINGS_URL, item_id=league_id))

def live_league(league_id): 
    """Return a live league by league_id"""
    ls = LeagueStandings(get_url(LEAGUES_CLASSIC_STANDINGS_URL, item_id=league_id))
    # Get this data once.
    gw = get_current_gameweek_id()
    players_json = get_url(PLAYERS_INFO_SUBURL) 
    livescore_json = get_url(GAMEWEEK_URL, item_id=gw, append=LIVE_SUBURL)  
    picks_in_league = []
    for team in ls.teams: 
        picks_json = get_url(ENTRY_BY_ID_URL, item_id=team.entry, append=(GAMEWEEK_URL + str(gw) + PICKS_SUBURL))
        history_json = get_url(ENTRY_BY_ID_URL, item_id=team.entry, append=ENTRY_HISTORY_SUBURL)
        #print(history_json)
        picks_in_league.append(Picks(picks_json, players_json, livescore_json, history_json, None))
    
    return LiveLeagueStandings(get_url(LEAGUES_CLASSIC_STANDINGS_URL, item_id=league_id), picks_in_league)

def live_points(team_id):
    """Return live points total and a table of players with live scores from the current Gameweek""" 
    gw = get_current_gameweek_id()
    players_json = get_url(PLAYERS_INFO_SUBURL) 
    livescore_json = get_url(GAMEWEEK_URL, item_id=gw, append=LIVE_SUBURL)  
    picks_json = get_url(ENTRY_BY_ID_URL, item_id=team_id, append=(GAMEWEEK_URL + str(gw) + PICKS_SUBURL))
    entry_info = entry(team_id)
    picks = Picks(picks_json, players_json, livescore_json, None, entry_info)
    return picks

def entry(team_id): # OK
    """Return a team entry"""
    return Entry(get_url(ENTRY_BY_ID_URL, item_id=team_id))


def teams(): # v.0.2
    """Return a real Premier League team with upcoming strenght scores for upcoming fixtures"""
    pass


def transfer_history(team_id): # v.0.2
    """Return the transfer history of the provided team entry"""
    pass


def fixtures(gw="upcoming"): # v.0.2
    """Return the fixtures for any Gameweek, defaults to the upcoming Gameweek"""
    pass

def gameweek(gw="current"): # v.0.2
    """Return information about a Gameweek, defaults to current Gameweek"""
    pass

def transfer_suggestions(): # v.0.3
    """Return suggested transfers based on expected points for next 5 Gameweeks"""
    pass

def get_url(target, item_id=None, append=None, auth=False):
    """
    Gets the data from the Fantasy Premier League API, specified by target, item_id and append.
    Authentication required for certain endpoints. 
    """
    url = FPL_URL + target   
    if item_id:
        url += '{}'.format(item_id)
    if append:
        url += '/{}'.format(append)
    response = requests.get(url)
    try:
        return response.json()
    except Exception:
        sys.exit("Game is being updated")