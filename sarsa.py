import random 
import operator

INIT_RANGE = 1

# Function to initizalize random values in a range
# Let's pick values between -1 and 1 for now
def init_state_qvalues(action_space):
    ret = {}
    for action in action_space:
        ret[action] = random.uniform(-INIT_RANGE, INIT_RANGE)
    return ret


class SARSA:

    # Let's structure the Q table as a dictionary
    # For each key (state), there is another dictionary (value)
    # In that second (value) dictionary, for each key (action) we have a Q-value
    # So, for example, self.qtable[state][action] corresponds to Q(state, action)

    def __init__(self, alpha, gamma, action_space, max_epsilon, min_epsilon, n_episodes):
        self.qtable = {}
        self.alpha = alpha 
        self.gamma = gamma 
        self.action_space = action_space # = ['up', 'down', 'left', 'right'] in GridWorld
        self.max_epsilon = max_epsilon
        self.min_epsilon = min_epsilon
        self.epsilon = max_epsilon
        self.episode = 0.0
        self.n_episodes = n_episodes

    

    def action(self, state):
        # Chance of taking random action
        if random.uniform(0,1) < self.epsilon:
            action = self.action_space[random.randint(0,3)]
            return action

        # Get (or initialize) the Q-values for the state
        if state in self.qtable:
            qvalues = self.qtable[state]
        else:
            qvalues = init_state_qvalues(self.action_space)
            self.qtable[state] = qvalues

        # Return action with the highest Q-value
        return max(qvalues.items(), key=operator.itemgetter(1))[0]

    def updateQValues(self, old_state, action, reward, new_state):
        ## Get the Q-values for the old state
        ## We might have to initialize the values if the action was randomly picked
        if old_state in self.qtable:
            qvalues = self.qtable[old_state]
        else:
            qvalues = init_state_qvalues(self.action_space)
            self.qtable[old_state] = qvalues       
        ### Old Q-value
        q_s_a =  qvalues[action]
        ## Q-value for the new state-action pair
        if new_state in self.qtable:
            new_state_qvalues = self.qtable[new_state]
        else:
            new_state_qvalues = init_state_qvalues(self.action_space)
            self.qtable[new_state] = new_state_qvalues
        ### Action with best Q-value for the new state USING OUR POLICY (HENCE SARSA BEING ON-POLICY!!!!)
        q_s1_a1 = new_state_qvalues[self.action(new_state)]

        # Update the values
        self.qtable[old_state][action] = q_s_a + self.alpha * (reward + self.gamma*q_s1_a1 - q_s_a)

    def reset(self):
        self.qtable = {}
        self.epsilon = self.max_epsilon
        self.episode = 0.0

    def update_epsilon(self):
        self.epsilon = self.max_epsilon - (self.max_epsilon - self.min_epsilon) * (self.episode/self.n_episodes)
        self.episode += 1



