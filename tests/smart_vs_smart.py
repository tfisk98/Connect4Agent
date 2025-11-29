import sys
import os
sys.path.append(os.getcwd())


from pettingzoo.classic import connect_four_v3


from src.agents.smart_agent import SmartAgent
import src.agents.random_agent as rnda
import src.game_facilities as gl

import numpy as np

### Testing RandomAgent with choose_action

gl.Connect4_game(100, SmartAgent, SmartAgent,  True )
