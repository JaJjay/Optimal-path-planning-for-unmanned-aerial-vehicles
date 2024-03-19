import pandas as pd
import numpy as np


def Q_learning():
    network = {(1, 2): 15, (1, 4): 25, (1, 3): 45, (2, 5): 30, (2, 4): 2, (5, 7): 2, (4, 7): 50, (4, 3): 2, (3, 6): 25,
               (6, 7): 1}
    Nodes = [1, 2, 3, 4, 5, 6, 7]

    np.random.seed(2)

    _state_num = len(Nodes)
    _actions = {
        1: [2, 3, 4], 2: [4, 5], 3: [6], 4: [3, 7], 5: [7], 6: [7], 7: []}
    org = 1
    des = 7
    MAX_action_num = len(Nodes)
    _epsilon = 0.9
    _learning_rate = 0.1
    _discount_factor = 0.9
    MAX_EPISODES = 100

    def build_Q_table(_state_num, Nodes, MAX_action_num):
        Q_table = pd.DataFrame(
            np.zeros((_state_num, MAX_action_num)),
            columns=Nodes,
            index=Nodes
        )

        return Q_table

    def choose_action(state_current, Q_table):
        action = None
        rand_num = np.random.uniform()
        candidate_actions = _actions[state_current]
        if (rand_num > _epsilon):
            action = np.random.choice(candidate_actions)
        else:
            max_Q_value = -np.inf
            for j in Nodes:
                if (Q_table.loc[state_current, j] > max_Q_value and j in candidate_actions):
                    max_Q_value = Q_table.loc[state_current, j]
                    action = j

        return action

    def get_env_feedback(state_current, action):
        arc = (state_current, action)
        max_length = max(list(network.values()))
        reward = max_length - network[arc]
        state_next = action
        return state_next, reward

    def solve_SPP_with_Q_table(org, des, Q_table):
        solution = [org]
        total_diatance = 0
        current_node = org
        while current_node != des:
            next_node = Q_table.loc[current_node, :].argmax() + 1
            solution.append(next_node)
            total_diatance += network[current_node, next_node]
            current_node = next_node

        return solution, total_diatance

    def Q_learning_algo():
        Q_table = build_Q_table(_state_num=_state_num, Nodes=Nodes, MAX_action_num=MAX_action_num)
        for episode in range(MAX_EPISODES):
            if (episode % 10 == 0):
                print('enter episode: {}'.format(episode), end='  ')
                # initial state
            state_current = org
            is_terminated = False
            if (episode % 10 == 0):
                print('current position: {}'.format(state_current), end='   ')
                print('next position: ', end='')

            step_counter = 0
            while not is_terminated:
                # choose next action
                action = choose_action(state_current, Q_table)
                state_next, reward = get_env_feedback(state_current, action)
                if (episode % 10 == 0):
                    print(' {} '.format(state_next), end='')

                Q_predict = Q_table.loc[state_current, action]
                Q_target = 0
                if (state_next != des):
                    Q_target = reward + _discount_factor * Q_table.loc[state_next,
                                                           :].max()
                else:
                    Q_target = reward
                    is_terminated = True
                Q_table.loc[state_current, action] += _learning_rate * (Q_target - Q_predict)
                state_current = state_next  # move to next state
                step_counter += 1

            if (episode % 10 == 0):
                print()
                print(Q_table, end='\n\n')

        return Q_table

    Q_table = build_Q_table(_state_num, Nodes, MAX_action_num)
    print(Q_table)
    Q_table = Q_learning_algo()
    print('Final Q_table: \n', Q_table, end='\n\n')
    solution, total_diatance = solve_SPP_with_Q_table(org, des, Q_table)
    result = str(solution) + str(total_diatance)
    return result


