class Fixture(object):
    def __init__(self, j):
        self.code = j['code']
        self.deadline_time = j['deadline_time']
        self.deadline_time_formatted = j['deadline_time_formatted']
        self.event = j['event']
        self.event_day = j['event_day']
        self.finished = j['finished']
        self.finished_provisional = j['finished_provisional']
        self.id_= j['id']
        self.kickoff_time = j['kickoff_time']
        self.kickoff_time_formatted = j['kickoff_time_formatted']
        self.minutes = j['minutes']
        self.provisional_start_time = j['provisional_start_time']
        self.started = j['started']
        self.team_a = j['team_a']
        self.team_a_difficulty = j['team_a_difficulty']
        self.team_a_score = j['team_a_score']
        self.team_h = j['team_h']
        self.team_h_difficulty = j['team_h_difficulty']
        self.team_h_score = j['team_h_score']
        self.stats = FixtureStats(j['stats'])

class FixtureStats(object): 
    """
    Contains live stats about a fixture. Each property is a dictionary on the form: 
    `{a: [{value: 1, element: 268}], h: [{value: 1, element: 423}]}`
    where element refers to the players/elements id. 
    """
    def __init__(self, j):
        self.goals_scored = j[0].get("goals_scored")
        self.assists = j[1]["asssist"]
        self.own_goals = j[2]["own_goals"]
        self.penalties_saved = j[3]["penalties_saved"] 
        self.penalties_missed = j[4]["penalties_missed"]
        self.yellow_cards = j[5]["yellow_cards"]
        self.red_cards = j[6]["red_cards"]
        self.saves = j[7]["saves"]
        self.bonus = j[8]["bonus"]
        self.bps = j[9]["bps"]
    
        


