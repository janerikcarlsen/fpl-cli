# Contributing to fpl-cli
If you see a bug, issue or want to submit a new feature to fpl-cli, 
please either file an issue in the GitHub issue tracker, or submit a Pull Request
* If it's a minor issue, please submit a Pull Request
* If it's a major feature, please file an issue before starting, so that others can contribute to the discussion.

# Developing fpl-cli
* Fork this repository, clone the fork and change directory to `fpl-cli`
* Create a virtualenv using python 2.7, 3.4, 3.5, 3.6 or 3.7, and activate that before running:
* `pip install -r requirements.txt`
* `pip install -r ci-requirements.txt`
* When running in a dev environment, set up an alias to be able to use the `fpl` shortcut. 
(This alias will automatically be installed as an entrypoint when you do a regular install via pip)
* `alias fpl='python -m fplcli.cli'`
* `fpl configure`

# Testing and style guides
* Unit tests are located in `tests/unit` folder, functional tests are located in `tests/functional` folder.
* The intention is for the code base to be compliant with flake8 with default configuration.

# Submitting a Pull Request
* Submit a Pull Request from your fork to the master branch of this repository. 