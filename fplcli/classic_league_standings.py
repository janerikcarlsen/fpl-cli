"""Contains classes for representing a Classic League Standings"""


class ClassicLeagueStandings(object):
    """Represent a team in a Classic League Standings"""
    def __init__(self, j):
        self.entry = j['entry']
        self.entry_name = j['entry_name']
        self.event_total = j['event_total']
        self.id_ = j['id']
        self.last_rank = j['last_rank']
        self.league = j['league']
        self.movement = j['movement']
        self.own_entry = j['own_entry']
        self.player_name = j['player_name']
        self.rank = j['rank']
        self.rank_sort = j['rank_sort']
        self.start_event = j['start_event']
        self.stop_event = j['stop_event']
        self.total = j['total']
