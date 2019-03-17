import unittest

from fplcli.constants import positions
from fplcli.constants import teams_long
from fplcli.constants import teams_short
from fplcli.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.json_input = mock_player_json()

    def test_player_init(self):
        p = Player(self.json_input)
        self.assertEqual(p.total_points, 203)
        self.assertEqual(p.minutes_played, 2553)
        self.assertEqual(p.total_points, 203)
        self.assertEqual(p.now_cost, 134)
        self.assertEqual(p.position, positions.get(3))
        self.assertEqual(p.points_per_game, float("6.8"))
        self.assertEqual(p.points_per_game_per_million, round(p.points_per_game / p.now_cost, 2))
        self.assertEqual(p.appearances, p.minutes_played / 90.0)
        self.assertEqual(p.first_name, "Mohamed")
        self.assertEqual(p.second_name, "Salah")
        self.assertEqual(p.id_, 253)
        self.assertEqual(p.photo, "118748.jpg")
        self.assertEqual(p.web_name, "Salah")
        self.assertEqual(p.team_code, 14)
        self.assertEqual(p.status, "a")
        self.assertEqual(p.code, 118748)
        self.assertEqual(p.squad_number, 11)
        self.assertEqual(p.news, "")
        self.assertEqual(p.news_added, "2018-10-20T15:31:16Z")
        self.assertEqual(p.chance_of_playing_this_round, 100)
        self.assertEqual(p.chance_of_playing_next_round, 100)
        self.assertEqual(p.value_form, "0.2")
        self.assertEqual(p.value_season , "15.1")
        self.assertEqual(p.cost_change_start, 4)
        self.assertEqual(p.cost_change_event, 0)
        self.assertEqual(p.cost_change_start_fall, -4)
        self.assertEqual(p.cost_change_event_fall, 0)
        self.assertEqual(p.in_dreamteam, True)
        self.assertEqual(p.dreamteam_count, 5)
        self.assertEqual(p.selected_by_percent, "44.7")
        self.assertEqual(p.form, "2.8")
        self.assertEqual(p.transfers_out, 2748829)
        self.assertEqual(p.transfers_in, 2365410)
        self.assertEqual(p.transfers_out_event, 14388)
        self.assertEqual(p.transfers_in_event, 223)
        self.assertEqual(p.event_points, 0)
        self.assertEqual(p.expected_this, "4.3")
        self.assertEqual(p.expected_next, "2.8")
        self.assertEqual(p.special, False)
        self.assertEqual(p.goals_scored, 17)
        self.assertEqual(p.assists, 9)
        self.assertEqual(p.clean_sheets, 17)
        self.assertEqual(p.goals_conceded, 15)
        self.assertEqual(p.own_goals, 0)
        self.assertEqual(p.penalties_saved, 0)
        self.assertEqual(p.penalties_missed, 0)
        self.assertEqual(p.yellow_cards, 0)
        self.assertEqual(p.red_cards, 0)
        self.assertEqual(p.saves, 0)
        self.assertEqual(p.bonus, 15)
        self.assertEqual(p.bps, 545)
        self.assertEqual(p.influence, "941.2")
        self.assertEqual(p.creativity, "798.7")
        self.assertEqual(p.threat, "1639.0")
        self.assertEqual(p.ict_index, "338.1")
        self.assertEqual(p.ea_index, 0)
        self.assertEqual(p.team, 12)
        self.assertEqual(p.team_name_long, teams_long[p.team])
        self.assertEqual(p.team_name, teams_short[p.team])

    def test_player_points_per_game(self):
        p = Player(self.json_input)
        self.assertEqual(p.points_per_90, round(p.total_points / p.appearances, 2))
        self.assertEqual(p.points_per_million, round(p.total_points / p.now_cost, 2))
        self.assertEqual(p.points_per_million_per_90, round(p.points_per_90 / p.now_cost, 2))
        self.assertEqual(p.bonus_per_90, round(p.bonus / p.appearances, 2))


def mock_player_json():
    return {
        "id": 253,
        "photo": "118748.jpg",
        "web_name": "Salah",
        "team_code": 14,
        "status": "a",
        "code": 118748,
        "first_name": "Mohamed",
        "second_name": "Salah",
        "squad_number": 11,
        "news": "",
        "now_cost": 134,
        "news_added": "2018-10-20T15:31:16Z",
        "chance_of_playing_this_round": 100,
        "chance_of_playing_next_round": 100,
        "value_form": "0.2",
        "value_season": "15.1",
        "cost_change_start": 4,
        "cost_change_event": 0,
        "cost_change_start_fall": -4,
        "cost_change_event_fall": 0,
        "in_dreamteam": True,
        "dreamteam_count": 5,
        "selected_by_percent": "44.7",
        "form": "2.8",
        "transfers_out": 2748829,
        "transfers_in": 2365410,
        "transfers_out_event": 14388,
        "transfers_in_event": 223,
        "loans_in": 0,
        "loans_out": 0,
        "loaned_in": 0,
        "loaned_out": 0,
        "total_points": 203,
        "event_points": 0,
        "points_per_game": "6.8",
        "ep_this": "4.3",
        "ep_next": "2.8",
        "special": False,
        "minutes": 2553,
        "goals_scored": 17,
        "assists": 9,
        "clean_sheets": 17,
        "goals_conceded": 15,
        "own_goals": 0,
        "penalties_saved": 0,
        "penalties_missed": 0,
        "yellow_cards": 0,
        "red_cards": 0,
        "saves": 0,
        "bonus": 15,
        "bps": 545,
        "influence": "941.2",
        "creativity": "798.7",
        "threat": "1639.0",
        "ict_index": "338.1",
        "ea_index": 0,
        "element_type": 3,
        "team": 12
    }
