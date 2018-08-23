from . import constants
from .league import LeagueEntry

class Entry(object):
    def __init__(self, j):
        if "entry" in j: 
            player = j['entry']  
        self.id_= player['id'] 
        self.player_first_name = player['player_first_name']
        self.player_last_name = player['player_last_name']
        self.player_region_id = player['player_region_id']
        self.player_region_name = player['player_region_name']
        self.player_region_short_iso = player['player_region_short_iso']
        self.summary_overall_points = player['summary_overall_points']
        self.summary_overall_rank = player['summary_overall_rank']
        self.summary_event_points = player['summary_event_points']
        self.summary_event_rank = player['summary_event_rank']
        self.joined_seconds = player['joined_seconds']
        self.current_event = player['current_event']
        self.total_transfers = player['total_transfers']
        self.total_loans = player['total_loans']
        self.total_loans_active = player['total_loans_active']
        self.transfers_or_loans = player['transfers_or_loans']
        self.deleted = player['deleted']
        self.email = player['email']
        self.joined_time = player['joined_time']
        self.name = player['name']
        self.bank = player['bank']
        self.value = player['value']
        self.kit = player['kit']
        self.event_transfers = player['event_transfers']
        self.event_transfers_cost = player['event_transfers_cost']
        self.extra_free_transfers = player['extra_free_transfers']
        self.strategy = player['strategy']
        self.favourite_team = player['favourite_team']
        self.started_event = player['started_event']
        self.player = player['player']
        self.leagues = []
        for league in j['leagues']['classic']:
            self.leagues.append(LeagueEntry(league))
            if league["name"] == 'Overall':
                self.overall_rank_movement = league["entry_movement"]
                self.overall_arrow = constants.arrows[self.overall_rank_movement]
                self.overall_last_rank = league["entry_last_rank"]
