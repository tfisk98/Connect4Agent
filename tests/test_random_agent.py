### Working directory must be the one of this file for src import to work

import sys
import os
sys.path.append(os.getcwd())

from pettingzoo.classic import connect_four_v3
import src.random_agent as rnda
import src.game_loop as gl


### Testing RandomAgent with choose_action

gl.Connect4_game(2, rnda.RandomAgent, rnda.RandomAgent,  True)


### Testing RandomAgent with choose_action_manual

env = connect_four_v3.env() # ou render_mode="rdb_array" ou bien None

env.reset(seed=42)
agent0=rnda.RandomAgent(env,env.agents[0])
agent1=rnda.RandomAgent(env,env.agents[1])
agent_list=[agent0,agent1]

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    current_agent=gl.select_current_agent(agent_list, agent)

    if termination or truncation:
        action = None
        if reward == 1:
            print(f"{agent} wins!\n")
        elif reward == 0:
            print("It's a draw!\n")
    else:
        # Take a random valid action
        action = current_agent.choose_action_manual(observation)
        gl.print_board(observation, env.agents, agent, action)

    env.step(action)

env.close()


### Getting data on numerous games beetween two random agent

data=gl.Connect4_game_with_data(10, rnda.RandomAgent, rnda.RandomAgent)

print(data[1][0])
print(data[1][1])
print(data[1][2])
