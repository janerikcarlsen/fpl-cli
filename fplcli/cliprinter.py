from prettytable import PrettyTable
import six
from pyfiglet import figlet_format
from . import constants

try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


def out(string, color="yellow", font="slant", figlet=False):
    """Outputs the provided string to the user in the console"""
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(
                string, font=font), color))
    else:
        six.print_(string)


def pretty_players(players): 
    """Formats a list of players"""
    fields = ["Id", "Name", "Position", "Total score", "Team", "Mins played", "Cost", "PPG", 
                "PPGM", "BPM", "PP90", "PPM", "PPGPM" ]
    table = PrettyTable(field_names=fields)
    table.align = "l"
    table.title = "Players"
    for p in players: 
        row = [p.id_, p.second_name[:20], p.position, p.total_points, constants.teams_long.get(p.team), 
                p.minutes_played, p.now_cost, p.points_per_game, p.points_per_game_per_million, 
                p.bonus_per_90, p.points_per_90, p.points_per_million, p.points_per_game_per_million]
        table.add_row(row)
    return table


def pretty_entry(team):
    """Formats a single team entry in a PrettyTable"""
    fields = ["Property", "Value"]
    table = PrettyTable(field_names=fields)
    table.align = "l"
    table.title = team.name + " - " + team.player_first_name + " " + team.player_last_name
    for attr, value in team.__dict__.items():
        if not attr == 'leagues':
            table.add_row([str(attr), str(value)])
    table.sortby = "Property"
    return table
    

def pretty_leagues(leagues):
    """Formats a list of leagues in a PrettyTable"""
    fields = ["Id", "League", "Arrow up/down", "Current rank", "Last rank"]
    table = PrettyTable(field_names=fields)
    table.align = "l"
    for l in leagues: 
        row = [l.id_, l.name, l.entry_arrow["unicode"], l.entry_rank, l.entry_last_rank]
        table.add_row(row)
    table.sortby = "Current rank" 
    table.align["Arrow up/down"] = 'c'   
    return table


def pretty_league(league): 
    """Formats a detailed league view in a PrettyTable"""   
    fields = ["Previous rank", "Current rank", "Arrow up/down", "Team name", "Manager name", 
                "Gameweek score", "Total score", "Team Id"] 
    table = PrettyTable(field_names=fields)
    table.title = league.name
    for t in league.teams:
        row = [t.last_rank, t.rank, t.arrow["unicode"], t.entry_name, t.player_name, 
                t.event_total, t.total, t.entry]
        table.add_row(row)
    table.sortby = "Current rank"
    table.align["Team name"] = 'l'
    table.align["Manager name"] = 'l'
    return table

def pretty_liveleague(league): 
    """Formats a detailed live league view in a PrettyTable"""   
    fields = ["Prev. rank", "Live rank", "Arrow", "Team name", "Manager name", "Captain", "Chip played", 
                "GW score", "Total score", "Prev. score", "Transfers", "Transfer hit", "Team Id"] 
    table = PrettyTable(field_names=fields)
    table.title = league.name
    for t in league.teams: 
        row = [ t.last_rank, 
                t.live_rank, 
                t.live_arrow["unicode"], 
                t.entry_name, 
                t.player_name, 
                t.picks.captain[:-4], 
                t.picks.display_chip, 
                t.picks.score, 
                t.live_total, 
                t.previous_gw_total, 
                "" if t.picks.entry_history.event_transfers == 0 else t.picks.entry_history.event_transfers, 
                "" if t.picks.entry_history.event_transfers_cost == 0 else t.picks.entry_history.event_transfers_cost, 
                t.entry
            ]
        table.add_row(row)
    table.sortby = "Live rank"
    table.align["Team name"] = 'l'
    table.align["Manager name"] = 'l'
    table.align["Captain"] = 'l'
    return table


def pretty_user(u): 
    """Formats a detailed single league view in a PrettyTable"""   
    fields = ["Id", "Overall rank", "Total score", "GW score", "GW rank", "GW Transfers", 
                "GW Hit", "Value", "Bank"] 
    table = PrettyTable(field_names=fields)
    table.title = u.team_name + " - " + u.first_name + " " + u.second_name
    row = [u.id_, u.overall_rank, u.overall_points, u.gameweek_points, u.gameweek_rank, 
            u.gameweek_transfers, u.gameweek_hit, u.team_value, u.bank ]
    table.add_row(row)
    return table


def pretty_picks_info(picks): 
    """Formats a detailed overview of the current live scores for a team in a Gameweek"""
    fields = ["Gameweek score", "Automatic subs", "Active chip", "Average Gameweek score", 
                "Highest Gameweek score", "Game updated", "Gameweek finished"]
    table = PrettyTable(field_names=fields)
    manager_name = picks.entry.player_first_name + " " + picks.entry.player_last_name
    table.title = picks.event.name +" - " + picks.entry.name + " - " + manager_name
    autosub_formatted = ""
    if picks.automatic_subs: 
        for autosub in picks.automatic_subs: 
            autosub_formatted += "Out: " + picks.players_data_indexed[autosub["element_out"]]["web_name"] + "\n"
            autosub_formatted += "In:  " + picks.players_data_indexed[autosub["element_in"]]["web_name"]
    table.add_row([picks.score, autosub_formatted , picks.active_chip, 
                    picks.event.average_entry_score, picks.event.highest_score, 
                    picks.event.data_checked, picks.event.finished])
    table.align = "c"
    table.align["Automatic subs"] = "l"
    return table


def pretty_picks_players(picks):
    """Formats a table of players picked for the gameweek, with live score information"""
    fields = ["Team", "Position", "Player", "Gameweek score", "Chance of playing next game", 
                "Player news", "Sub position", "Id"]    
    table = PrettyTable(field_names=fields)
    table.title = "GW points: " + str(picks.score) \
                + "  -  Average GW points: " + str(picks.event.average_entry_score) \
                + "  -  Overall arrow: " + picks.entry.overall_arrow["unicode"] \
                + "  -  GW rank: " + str(picks.entry.summary_event_rank) \
                + "  -  Overall rank: " + str(picks.entry.summary_overall_rank)
    for p in picks.picks: 
        if picks.player_fielded[p.pick_position]:
            table.add_row([p.team_name, p.position, p.displayname, p.gw_points, 
                            p.chance_of_playing_next_round, p.news, p.pick_position, p.id_])
    table.add_row(["===", "===", "=======", "==", "", "", "==", "==="])
    for p in picks.picks: 
        if not picks.player_fielded[p.pick_position]:
            table.add_row([p.team_name, p.position, p.displayname, p.gw_points, 
                            p.chance_of_playing_next_round, p.news, p.pick_position, p.id_])
    table.align = "l"
    table.align["Gameweek score"] = "r"
    table.align["Sub position"] = "r"
    table.align["Chance of playing next game"] = "c"
    return table
