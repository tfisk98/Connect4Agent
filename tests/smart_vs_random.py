import sys
import os
sys.path.append(os.getcwd())


from pettingzoo.classic import connect_four_v3


from src.smart_agent import SmartAgent
import src.random_agent as rnda
import src.game_loop as gl

import numpy as np

### Testing RandomAgent with choose_action

gl.Connect4_game(100, SmartAgent, rnda.RandomAgent,  True )

print("SmartAgent is Agent0 and RandomAgent is Agent1")




### Testing RandomAgent with choose_action_manual

"""

env = connect_four_v3.env(render_mode="human") # ou render_mode="rdb_array" ou bien None

env.reset(seed=42)
agent0=SmartAgent(env,env.agents[0])
agent1=rnda.RandomAgent(env,env.agents[1])
agent_list=[agent0,agent1]
moves = 4*[0]

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    current_agent=gl.select_current_agent(agent_list, agent)

    if termination or truncation:
        action = None
        if reward == 1:
            print(f"{agent} wins!")
        elif reward == 0:
            print("It's a draw!")
    else:
        # Take a random valid action
        action = current_agent.choose_action_manual(observation)
        print(f"{agent} plays column {action}")

    env.step(action)

env.close()
"""