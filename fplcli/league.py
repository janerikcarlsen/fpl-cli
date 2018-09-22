from builtins import super
from . import constants

class LeagueEntry(object): 
    def __init__(self, j): 
        self.id_= j['id']
        self.entry_rank = j['entry_rank']
        self.entry_last_rank = j['entry_last_rank']
        self.entry_movement = j['entry_movement']
        self.entry_arrow = constants.arrows[self.entry_movement]
        self.entry_change = j['entry_change']
        self.entry_can_leave = j['entry_can_leave']
        self.entry_can_admin= j['entry_can_admin']
        self.entry_can_invite= j['entry_can_invite']
        self.entry_can_forum = j['entry_can_forum']
        self.entry_code= j['entry_code']
        self.name = j['name']
        self.short_name = j['short_name']
        self.created = j['created']
        self.closed = j['closed']
        self.forum_disabled = j['forum_disabled']
        self.make_code_public = j['make_code_public']
        self.rank = j['rank']
        self.size = j['size']
        self.league_type = j['league_type']
        self._scoring = j['_scoring']
        self.reprocess_standings = j['reprocess_standings']
        self.admin_entry = j['admin_entry']
        self.start_event = j['start_event']
        

class EntryInLeague(object):
    def __init__(self, j, picks=None):
        self.id_= j['id']
        self.entry_name = j['entry_name']
        self.player_name = j['player_name']
        self.rank = j['rank']
        self.event_total = j['event_total']
        self.movement = j['movement']
        self.arrow = constants.arrows[self.movement]
        self.own_entry = j['own_entry']
        self.last_rank = j['last_rank']
        self.rank_sort = j['rank_sort']
        self.total = j['total']
        self.entry = j['entry']
        self.league = j['league']
        self.start_event = j['start_event']
        self.stop_event = j['stop_event']
        # Live score information 
        self.picks = picks
        self.previous_gw_total = None
        self.rank_previous = None
        self.event_transfers_costs = None
        self.live_total = None
        self.live_movement = None
        self.live_arrow = None
        self.live_rank = None
    
    def resolve_live_movement(self): 
        if self.movement is "new": 
            self.live_movement = "new"
        elif self.live_rank < self.last_rank: 
            self.live_movement = "up"
        elif self.live_rank > self.last_rank: 
            self.live_movement = "down"
        else: 
            self.live_movement = "same"

        self.live_arrow = constants.arrows[self.live_movement]

class LeagueStandings(object):
    def __init__(self, j):
        self.name = j['league']['name']
        self.id_ = j['league']['id']
        self.teams = []
        for team in j['standings']['results']:
            self.teams.append(EntryInLeague(team))

class LiveLeagueStandings(LeagueStandings):
    def __init__(self, j, picks_in_league):
        super().__init__(j)
        for team in self.teams:
            team.picks = next((picks for picks in picks_in_league if picks.entry_history.entry == team.entry), None)
            # Recalculate live standings based on history 
            # Get the live total for each team
            current_gw = int(team.picks.event.id_)
            team.previous_gw_total = team.picks.complete_entry_history[current_gw - 2].total_points
            # Get this gameweek transfer cost for each team
            team.event_transfers_costs = team.picks.complete_entry_history[current_gw - 1].event_transfers_cost
            team.live_total = team.previous_gw_total + team.picks.score - team.event_transfers_costs
            
        # Get the updated rank for live league
        self.teams.sort(key=lambda x:x.live_total, reverse=True)
        for i, team in enumerate(self.teams): 
            team.live_rank = i + 1
            team.resolve_live_movement()

