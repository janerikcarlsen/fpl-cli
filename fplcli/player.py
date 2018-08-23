from . import constants

class Player(object):     
    def __init__(self, j):
        self.total_points = j["total_points"]
        self.minutes_played = j["minutes"]
        self.total_points = j["total_points"]
        self.now_cost = j["now_cost"]
        self.minutes_played = j["minutes"]
        self.position = constants.positions.get(j["element_type"])
        self.points_per_game = float(j["points_per_game"])
        self.points_per_game_per_million = round(self.points_per_game / self.now_cost, 2)
        self.appearances = self.minutes_played / 90.0
        self.first_name = j["first_name"]
        self.second_name = j["second_name"]
        self.id_ = j["id"]
        self.photo = j["photo"]
        self.web_name = j["web_name"]
        self.team_code = j["team_code"]
        self.status = j["status"]
        self.code = j["code"]
        self.squad_number = j["squad_number"]
        self.news = j["news"]
        self.news_added = j["news_added"]              
        self.chance_of_playing_this_round = j["chance_of_playing_this_round"] if j["chance_of_playing_this_round"] else ""
        self.chance_of_playing_next_round = j["chance_of_playing_next_round"] if j["chance_of_playing_next_round"] else ""
        self.value_form = j["value_form"]
        self.value_season = j["value_season"]
        self.cost_change_start = j["cost_change_start"]
        self.cost_change_event = j["cost_change_event"]
        self.cost_change_start_fall = j["cost_change_start_fall"]
        self.cost_change_event_fall = j["cost_change_event_fall"]
        self.in_dreamteam = j["in_dreamteam"]
        self.dreamteam_count = j["dreamteam_count"]
        self.selected_by_percent = j["selected_by_percent"]
        self.form = j["form"]
        self.transfers_out = j["transfers_out"]
        self.transfers_in = j["transfers_in"]
        self.transfers_out_event = j["transfers_out_event"]
        self.transfers_in_event = j["transfers_in_event"]
        self.event_points = j["event_points"] 
        self.expected_this = j["ep_this"] # Float
        self.expected_next = j["ep_next"] # Float
        self.special = j["special"] # Boolean
        self.goals_scored = j["goals_scored"]
        self.assists = j["assists"]
        self.clean_sheets = j["clean_sheets"]
        self.goals_conceded = j["goals_conceded"]
        self.own_goals = j["own_goals"]
        self.penalties_saved = j["penalties_saved"]
        self.penalties_missed = j["penalties_missed"]
        self.yellow_cards = j["yellow_cards"]
        self.red_cards = j["red_cards"]
        self.saves = j["saves"]
        self.bonus = j["bonus"]
        self.bps = j["bps"]
        self.influence = j["influence"]
        self.creativity = j["creativity"]
        self.threat = j["threat"]
        self.ict_index = j["ict_index"]
        self.ea_index = j["ea_index"]
        self.team = j["team"]
        self.team_name_long = constants.teams_long[self.team]
        self.team_name = constants.teams_short[self.team]
     
        if self.appearances == 0:
            self.points_per_90, self.points_per_million, self.points_per_million_per_90, self.bonus_per_90 = [0,0,0,0]
        else: 
            self.points_per_90 = round(self.total_points/ self.appearances, 2)
            self.points_per_million = round(self.total_points / self.now_cost, 2)
            self.points_per_million_per_90 = round(self.points_per_90 / self.now_cost, 2)
            self.bonus_per_90 = round(j["bonus"] / self.appearances, 2)

    def __str__(self): 
        return "\t".join([((str(self.second_name)[:13])+ "  "), str(self.position), str(self.total_points), 
            str(self.minutes_played), str(self.now_cost), str(self.points_per_game), 
            str(self.points_per_game_per_million), str(self.bonus_per_90), str(self.points_per_90), 
            str(self.points_per_million), str(self.points_per_game_per_million)])
