import os
from configparser import ConfigParser
from builtins import input

def get_config():
    config = ConfigParser()
    filename = os.path.expanduser("~/.fpl/config")
    config.read(filename)
    return config

def configure(): 
    """Configure FPL CLI. Saves the team_id to ~/.fpl/config"""
    config = ConfigParser()
    team_id = ''
    filename = os.path.expanduser("~/.fpl/config")
    try: 
        config.read(filename)
        team_id = config['DEFAULT']['team_id']
    except Exception:
        print("No existing configuration found, proceeding")
    
    team_id = input("FPL team_id [ " + team_id +" ]: ") or team_id
    config['DEFAULT'] = {}
    config['DEFAULT']['team_id'] = team_id

    # Store to ~/fpl/config: 
    update_config(config, filename)           

def update_config(config, filename):
    """Update config file with new values"""
    if not os.path.isfile(filename):
        _create_file(filename)
    with open(filename, 'r') as f:
        contents = f.readlines()
    with open(filename, 'w') as f:
            config.write(f)


def _create_file(config_filename):
    # Create the file as well as the parent dir if needed.
    dirname = os.path.split(config_filename)[0]
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    with os.fdopen(os.open(config_filename,
                    os.O_WRONLY | os.O_CREAT, 0o600), 'w'):
        pass
