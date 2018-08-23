"""
Contains classes representing information about a selection of picked players for a 
team entry for a gameweek
"""

import future
from builtins import super
from .gameweek import Gameweek
from .player import Player

class Picks(object):
    """Contain the picks (selected players) for a team entry for a given gameweek"""
    def __init__(self, j, players_data, livescore_data, complete_entry_history, entry):
        self.active_chip = j['active_chip']
        self.automatic_subs = j['automatic_subs'] if j['automatic_subs'] else ""
        self.entry_history = EntryHistory(j['entry_history'])
        self.event = Gameweek(j['event'])
        self.entry = entry if entry else complete_entry_history["entry"]
        if complete_entry_history:
            # Needed to reprocess a live league's standings
            self.complete_entry_history = {eh['entry']: eh for eh in complete_entry_history['history']}

        self.complete_entry_history = {}
        self.picks = []
        self.players_data_indexed = {player_data['id']: player_data for i, player_data in enumerate(players_data)}
        for pick in j['picks']:
            self.picks.append(PickedPlayer(pick, self.players_data_indexed[pick['element']], self))
        self.player_fielded = {
            1: True,
            2: True,
            3: True,
            4: True,
            5: True,
            6: True,
            7: True,
            8: True,
            9: True,
            10: True,
            11: True, 
            12: False, 
            13: False, 
            14: False, 
            15: False
        }
        self.score = self.resolve_score(livescore_data["elements"])

    def resolve_score(self, livescore_element):
        if self.active_chip:
            if self.active_chip == "bboost":
                for i in [12, 13, 14, 15]: 
                    self.player_fielded[i] = True
        if self.automatic_subs:
            for autosub in self.automatic_subs: 
                sub_out = next((pick for pick in self.picks if pick.id_ == autosub["element_out"]), None)
                sub_in = next((pick for pick in self.picks if pick.id_ == autosub["element_in"]), None)
                self.player_fielded[sub_out.pick_position] = False
                self.player_fielded[sub_in.pick_position] = True
        
        gw_score = 0
        for pick in self.picks:
            pick.gw_points = pick.multiplier * livescore_element[str(pick.id_)]["stats"]["total_points"]
            pick.stats = livescore_element[str(pick.id_)]["stats"]
            if self.player_fielded[pick.pick_position]:
                gw_score += pick.gw_points
        return gw_score


class PickedPlayer(Player):
    def __init__(self, j, player_data, picks):
        super().__init__(player_data)
        self.id_ = j['element']
        self.is_captain = j['is_captain']
        self.is_vice_captain = j['is_vice_captain']
        self.multiplier = j['multiplier']
        self.pick_position = j['position']
        self.gw_points = None
        self.stats = None
        self.displayname = self.resolve_name(picks)

    def resolve_name(self, picks):
        displayname = self.web_name
        if self.is_captain:
            displayname += " (c)"
        if self.is_vice_captain:
            displayname +=  " (vc)"
        if self.is_captain and picks.active_chip == "3xc":
            displayname += " (TC)"
        return displayname

class EntryHistory(object):
    def __init__(self, j):
        self.bank = j['bank']
        self.entry = j['entry']
        self.event = j['event']
        self.event_transfers = j['event_transfers']
        self.event_transfers_cost = j['event_transfers_cost']
        self.id_ = j['id']
        self.movement = j['movement']
        self.overall_rank = j['overall_rank']
        self.points = j['points']
        self.points_on_bench = j['points_on_bench']
        self.rank = j['rank']
        self.rank_sort = j['rank_sort']
        self.targets = j['targets']
        self.total_points = j['total_points']
        self.value = j['value']
