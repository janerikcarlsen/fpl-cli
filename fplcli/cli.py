import os
import sys
import click
from . import fplapi
from . import configure as conf
from .cliprinter import out
from .cliprinter import pretty_league
from .cliprinter import pretty_liveleague
from .cliprinter import pretty_leagues
from .cliprinter import pretty_picks_info
from .cliprinter import pretty_picks_players
from .cliprinter import pretty_players
from .cliprinter import pretty_entry


def get_team_id():
    try: 
        config = conf.get_config()
        return config["DEFAULT"]["team_id"]
    except KeyError: 
        sys.exit("FPL CLI is not configured. Type: fpl configure")

@click.group()
def main():
    """
    FPL CLI -  Command Line Interface for Fantasy Premier League.
    """
    out("FPL CLI", color="cyan", figlet=True)
    out("FPL CLI - Fantasy Premier League in your terminal \n", color="red")


@main.command()
def players():
    """Returns all players"""
    players = fplapi.players()
    out(pretty_players(players))


@main.command()
def leagues():
    """Returns all leagues for my team entry"""
    leagues = fplapi.leagues_entered(get_team_id())
    out(pretty_leagues(leagues))


@main.command()
@click.argument("league_id")
def league(league_id):
    """Returns confirmed scores for a league by id"""
    league = fplapi.league(league_id)
    out(pretty_league(league))


@main.command()
@click.argument("league_id")
def liveleague(league_id):
    """Returns live scores for a league by id"""
    league = fplapi.live_league(league_id)
    out(pretty_liveleague(league))


@main.command()
def entry():
    """
    Returns information about your team entry,
    using the team_id as configured in 'fpl configure'
    """
    my_entry = fplapi.entry(get_team_id())
    out(pretty_entry(my_entry))


@main.command()
def points():
    """Returns live points for your team"""
    picks = fplapi.live_points(get_team_id())
    out(pretty_picks_info(picks))
    out(pretty_picks_players(picks))


@main.command()
def configure():
    """
    Set up team_id (required)
    """
    conf.configure()
    out("fpl-cli configured. Type 'fpl' for instructions")


if __name__ == '__main__':
    main()
