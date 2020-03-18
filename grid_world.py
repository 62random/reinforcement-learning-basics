from PIL import Image, ImageDraw, ImageColor
from IPython.display import display

class GridWorld:
    def __init__(self, rows, cols, win, lose_states, obstacles, start):
        # Variáveis Globais 
        self.BOARD_ROWS = rows
        self.BOARD_COLS = cols
        self.WIN_STATE = win
        self.LOSE_STATES = lose_states
        self.OBSTACLES = obstacles
        self.START = start
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

    def render(self):
        width = 600
        cell_width = int(width/self.BOARD_COLS)
        cell_height = int(cell_width)
        height = cell_height * self.BOARD_ROWS
        

        image = Image.new(mode='RGB', size=(width, height), color='white')

        draw = ImageDraw.Draw(image)
        for i in range(self.BOARD_COLS - 1):
            vertical_line = ((i*cell_width + cell_width, 0),(i*cell_width + cell_width, image.height))
            draw.line(vertical_line, fill='black')

        for i in range(self.BOARD_ROWS - 1):
            horizontal_line = ((0, i*cell_height + cell_height),(image.width, i*cell_height + cell_height))
            draw.line(horizontal_line, fill='black')

        convert_pos = lambda a: (a[1]*cell_width, a[0]*cell_height)
        square = lambda a: [(a[0], a[1]), (a[0] + cell_width, a[1] + cell_height)]

        for p in self.OBSTACLES:
            draw.rectangle(square(convert_pos(p)), fill='black')
        
        for p in self.LOSE_STATES:
            draw.rectangle(square(convert_pos(p)), fill='red')
        
        draw.rectangle(square(convert_pos(self.WIN_STATE)), fill='green')

        draw.rectangle(square(convert_pos(self.START)), fill='yellow')
        
        del draw
        return display(image)

