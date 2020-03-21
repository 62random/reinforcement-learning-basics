import random 
# This is just a class meant to run any TD (time difference) reinforcement learning algorithm
# We'll need an environment and a learning model
# The environment can be something as simple as 'Grid World' or maybe something like an atari game (as provided by OpenAI Gym)


class Runner:
    def __init__(self, environment, learning_model):
        self.env = environment
        self.model = learning_model

    def run(self, n_episodes):
        self.env.reset()
        self.model.reset()

        # Data about the rounds
        steps_taken = []
        paths = []

        # This data variable is a general purpose 'data collector'
        # in Grid World I use it to track which games finish in a winning state
        # However, other games might not have a winning state (pacman for example)
        # So i decided to just give it the generic name 'data'
        # You might want to change it to better fit your purpose
        data = []
        # Make N_EPISODES rounds of the game
        for i in range(n_episodes): 
            finished = False
            state = self.env.state            
            path = [state]
            while not finished:                
                # Register old state, to later use to update q-values
                old_state = state
                # Predict an action with our model 
                action = self.model.action(self.env.state)
                # Make th move in the environment
                state, reward, finished, steps = self.env.step(action)
                if i > n_episodes -5:
                    path.append(state)

                # Update Q-values
                self.model.updateQValues(old_state, action, reward, state)
            # Update epsilon (so the exploitation grows)
            self.model.update_epsilon()
            # Collect data
            steps_taken.append(steps)
            data.append(state == self.env.WIN_STATE) 
            self.env.reset()
            if i > n_episodes - 5:
                paths.append(path)
        
        return steps_taken, data, paths
