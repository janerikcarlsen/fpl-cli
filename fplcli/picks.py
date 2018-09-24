"""
Contains classes representing information about a selection of picked players for a 
team entry for a gameweek
"""

import sys
import future
from builtins import super
from .gameweek import Gameweek
from .player import Player
from .constants import chips

class Picks(object):
    """Contain the picks (selected players) for a team entry for a given gameweek"""
    def __init__(self, j, players_data, livescore_data, complete_entry_history, entry):
        self.active_chip = j['active_chip']
        self.display_chip = chips[self.active_chip] if self.active_chip else ""
        self.automatic_subs = j['automatic_subs'] if j['automatic_subs'] else ""
        self.entry_history = EntryHistory(j['entry_history'])
        self.event = Gameweek(j['event'])
        self.entry = entry if entry else complete_entry_history["entry"]
        if complete_entry_history:
            # Needed just for live league standings
            self.complete_entry_history = [EntryHistory(eh) for eh in complete_entry_history['history']]
        self.picks = []
        self.captain = None
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
        self.provisional_bonus = self.resolve_provisional_bonus(livescore_data)
        self.score = self.resolve_score(livescore_data["elements"])

    def resolve_provisional_bonus(self, livescore_data): 
        provisional_bonus = {}
        for fixture in livescore_data["fixtures"]: 
            # If bonus points not confirmed
            if fixture["started"] and not fixture["finished"]:
                if not (fixture["stats"][8]["bonus"]["a"] or fixture["stats"][8]["bonus"]["h"]): 
                    bps = []
                    for data in fixture["stats"][9]["bps"]["a"]:
                        bps.append(data)
                    for data in fixture["stats"][9]["bps"]["h"]:
                        bps.append(data)
                bps.sort(key=lambda x:x["value"], reverse=True)
                
                available_bonus = 3
                last_bps = sys.maxsize
                last_points = 3
                for player in bps: 
                    if player['value'] == last_bps: 
                        provisional_bonus[player["element"]] = last_points
                        available_bonus -= 1
                    elif available_bonus > 0: 
                        provisional_bonus[player["element"]] = available_bonus
                        last_points = available_bonus
                        available_bonus -= 1
                        last_bps = player["value"]
                    else: 
                        break
        return provisional_bonus

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
            if pick.is_captain: 
                self.captain = pick.displayname
            pick.gw_points = pick.multiplier * livescore_element[str(pick.id_)]["stats"]["total_points"]
            # Add provisional bonus
            pick.gw_points += pick.multiplier * self.get_provisional_bonus(pick)
            pick.stats = livescore_element[str(pick.id_)]["stats"]
            if self.player_fielded[pick.pick_position]:
                gw_score += pick.gw_points
        return gw_score

    def get_provisional_bonus(self, pick): 
        # return provisional bonus if has any, 0 otherwise. 
        if pick.id_ in self.provisional_bonus: 
            return self.provisional_bonus[pick.id_]
        else:
            return 0


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
