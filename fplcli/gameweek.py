class Gameweek(object):
    def __init__(self, j):
        self.average_entry_score = j['average_entry_score']
        self.data_checked = j['data_checked']
        self.deadline_time = j['deadline_time']
        self.deadline_time_epoch = j['deadline_time_epoch']
        self.deadline_time_formatted = j['deadline_time_formatted']
        self.deadline_time_game_offset = j['deadline_time_game_offset']
        self.finished = j['finished']
        self.highest_score = j['highest_score']
        self.highest_scoring_entry = j['highest_scoring_entry']
        self.id_ = j['id']
        self.is_current = j['is_current']
        self.is_next = j['is_next']
        self.is_previous = j['is_previous']
        self.name = j['name']

        