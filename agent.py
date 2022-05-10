import torch
import numpy as np 
import random 
from snake_ai import SnakeGameAI, Direction, Point
from collections import deque 

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 1e-3

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0 #discount rate
        self.memory = deque(maxlen=MAX_MEMORY) 
        #model, trainer 

    def get_state(self, game):
        pass

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self, state, action, reward, next_state, done):
        pass 

    def get_action(self, state):
        pass

def train():
    plot_score = []
    plot_mean_score = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()
    while True:
        pass 
        state_old = agent.get_state(game)

        #get move
        final_move = agent.get_action(state_old)

        #perform move and get new state
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        #train short memory 
        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            # train long memory, plot result 
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()
            if score >  record:
                record = score 
                #agent.mode.save()

            print('Game', agent.n_games, 'Score', score, 'Record:', record )

if __name__ == "__main__":
    train()