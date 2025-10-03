import time
import math
import random
import numpy as np
from helper import *


class AIPlayer:

    def __init__(self, player_number: int, timer):
        """
        Intitialize the AIPlayer Agent

        # Parameters
        `player_number (int)`: Current player number, num==1 starts the game
        
        `timer: Timer`
            - a Timer object that can be used to fetch the remaining time for any player
            - Run `fetch_remaining_time(timer, player_number)` to fetch remaining time of a player
        """
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}: ai'.format(player_number)
        self.timer = timer

    def get_move(self, state: np.array) -> Tuple[int, int]:
        """
        Given the current state of the board, return the next move

        # Parameters
        `state: Tuple[np.array]`
            - a numpy array containing the state of the board using the following encoding:
            - the board maintains its same two dimensions
            - spaces that are unoccupied are marked as 0
            - spaces that are blocked are marked as 3
            - spaces that are occupied by player 1 have a 1 in them
            - spaces that are occupied by player 2 have a 2 in them

        # Returns
        Tuple[int, int]: action (coordinates of a board cell)
        """

        # Do the rest of your implementation here
        raise NotImplementedError('Whoops I don\'t know what to do')
    
    import time
import math
import random
import numpy as np
from helper import *


class AIPlayer:

    def _init_(self, player_number: int, timer):
        """
        Intitialize the AIPlayer Agent

        # Parameters
        player_number (int): Current player number, num==1 starts the game
        
        timer: Timer
            - a Timer object that can be used to fetch the remaining time for any player
            - Run fetch_remaining_time(timer, player_number) to fetch remaining time of a player
        """
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}: ai'.format(player_number)
        self.timer = time
    def get_move(self, state: np.array) -> Tuple[int, int]:
        """
        Given the current state of the board, return the next move

        # Parameters
        state: Tuple[np.array]
            - a numpy array containing the state of the board using the following encoding:
            - the board maintains its same two dimensions
            - spaces that are unoccupied are marked as 0
            - spaces that are blocked are marked as 3
            - spaces that are occupied by player 1 have a 1 in them
            - spaces that are occupied by player 2 have a 2 in them

        # Returns
        Tuple[int, int]: action (coordinates of a board cell)
        """

        # Do the rest of your implementation here

        move = self.maxi(state)
        return (move[1],move[2])

    def maxi(self,state: np.array) -> Tuple[int, int, int]:
        next_possible_states = get_valid_actions(state, self.player_number)
        if(len(next_possible_states)==1):
            x,y=check_win(state,next_possible_states[0],self.player_number)
            if(x):
                return (1,next_possible_states[0][0],next_possible_states[0][1])
            else:
                return (0,next_possible_states[0][0],next_possible_states[0][1])
        next_moves = Tuple[int,int,int]
        zero = Tuple[int,int,int]
        p=0
        for move in next_possible_states:
            i,j = move
            state[i][j] = self.player_number
            next_moves=self.mini(state)
            state[i][j] = 0
            if next_moves[0] == 1:
                return (1,i,j)
            elif next_moves[0] == 0:
                zero = (0,i,j)
                p=1
        if p==1:
            return zero
        else:
            a,b = next_possible_states[0]
            return (-1,a,b)

    def mini(self,state: np.array) -> Tuple[int, int, int]:
        next_possible_states = get_valid_actions(state)
        if(len(next_possible_states)==1):
            if(self.player_number==1):
                x,y=check_win(state,next_possible_states[0],2)
            else:
                x,y=check_win(state,next_possible_states[0],1)
            if(x):
                return (-1,next_possible_states[0][0],next_possible_states[0][1])
            else:
                return (0,next_possible_states[0][0],next_possible_states[0][1])
        next_moves = Tuple[int,int,int]
        zero = Tuple[int,int,int]
        p=0
        for move in next_possible_states:
            i,j = move
            if(self.player_number==1):
                state[i][j] = 2
            else:
                state[i][j] = 1
            next_moves=self.maxi(state)
            state[i][j] = 0
            if next_moves[0] == -1:
                return (-1,i,j)
            elif next_moves[0] == 0:
                zero = (0,i,j)
                p=1
        if p==1:
            return zero
        else:
            a,b = next_possible_states[0]
            return (1,a,b)


