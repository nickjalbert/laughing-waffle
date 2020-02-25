# laughing-waffle

Basic implementation of an OpenAI gym environment and solution using RLlib+Ray.

The environment (CorridorEnv) models a 1D hallway in which you can move left or
right.  The goal is to walk the length of the environment.

# Dev setup

Developed on OS X 10.15.2 with Python 3.7.6.

* `virtualenv -p /usr/local/bin/python3 laughing-waffle`
* `source laughing-waffle/bin/activate`
* `pip install -r requirements.txt`


Example command line rllib test: `rllib train --run=PPO --env=CartPole-v0`

Solve corridor: `python solve.py`
