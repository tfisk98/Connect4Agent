from pettingzoo.classic import connect_four_v3

import src.random_agent as rnda

env = connect_four_v3.env(render_mode="human") # ou render_mode="rdb_array" ou bien None

env.reset(seed=42)

agent0=rnda.RandomAgent(env,env.agents[0])
agent1=rnda.RandomAgent(env,env.agents[1])
agent_list=[agent0,agent1]

### Testing RandomAgent with choose_action

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if agent_list[0].name==agent :
        current_agent=agent_list[0]

    else :
        current_agent=agent_list[1]

    if termination or truncation:
        action = None
        if reward == 1:
            print(f"{agent} wins!")
        elif reward == 0:
            print("It's a draw!")
    else:
        # Take a random valid action
        action = current_agent.choose_action(observation)
        print(f"{agent} plays column {action}")

    env.step(action)


### Testing RandomAgent with choose_action_manual

env.reset(seed=42)

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if agent_list[0].name==agent :
        current_agent=agent_list[0]

    else :
        current_agent=agent_list[1]

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
