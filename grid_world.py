class GridWorld:
    def __init__(self, rows, cols, win, lose_states, obstacles, start, deterministic):
        # Variáveis Globais 
        self.BOARD_ROWS = rows
        self.BOARD_COLS = cols
        self.WIN_STATE = win
        self.LOSE_STATES = lose_states
        self.OBSTACLES = obstacles
        self.START = start
        self.DETERMINISTIC = deterministic
        self.action_space = ['up', 'down', 'left', 'right']

        self.state = self.START
        self.steps = 0
        self.rewards = {}
        self.rewards[self.WIN_STATE] = 1        
        for lose in self.LOSE_STATES:
            self.rewards[lose] = -1
        self.step_reward = 0
    
    def reward(self):
        t = self.step_reward
        self.step_reward = 0
        return self.rewards.get(self.state, 0) + t

    def nextPosition(self, action):
        if action is "up":
            new_pos = (self.state[0] - 1, self.state[1])
        elif action is "down":
            new_pos = (self.state[0] + 1, self.state[1])
        elif action is "left":
            new_pos = (self.state[0], self.state[1] - 1)
        elif action is "right":
            new_pos = (self.state[0], self.state[1] + 1)
        else: # just go up
            new_pos = (self.state[0] -1, self.state[1])
        
        if  new_pos in self.OBSTACLES or \
            new_pos[0] < 0 or \
            new_pos[0] > self.BOARD_ROWS - 1 or \
            new_pos[1] < 0 or \
            new_pos[1] > self.BOARD_COLS - 1:
            
            self.step_reward = -0.1
        
            return self.state

        return new_pos

    def step(self, action):
        self.steps += 1
        self.state = self.nextPosition(action)

        finished = False

        if self.state == self.WIN_STATE  or self.state in self.LOSE_STATES:
            finished = True

        return self.state, self.reward(), finished, self.steps

    def reset(self):
        self.state = self.START
        self.steps = 0
        self.step_reward = 0
