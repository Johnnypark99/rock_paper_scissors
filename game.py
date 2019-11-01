import random

# Game class, has the options, a session tracker and the game state
class Game():
    options = ['rock', 'paper', 'scissors'] # list of choices
    sessions = 0 # tracker for amount of games played
    __state = None # game state (this attribute is private so it can not be modified by accident)
    
    def __init__(self): # constructor that starts the game
        self.__state = True

    def close(self): # method to close the game
        self.__state = False

    def get_state(self): # method to get the current state of the game
        return self.__state
    
    def get_sessions(self): # method to return the amount of times game has ran
        return self.sessions

# Player class, inherits from Game class
class Player(Game):
    choice = None 
 
    def __init__(self): # constructor that sets the name to 'Human'
        self.name = 'Human'

    def set_choice(self): # get the choice from the human player
        print(f'Select from rock, paper or scissors')
        self.choice = input('Input your choice: ')

    def get_choice(self): # return the choice
        return self.choice

# AiPlayer class, inherits from Player class
class AiPlayer(Player):
    def __init__(self):
        self.name = 'AI' # constructor that sets the name to 'Human'
    
    def set_choice(self): # set the choice for AI and return it
        self.choice = self.options[random.randint(0,2)]
        return self.choice

# main function
def main():
    game = Game() # initialize the Game object
    human = Player() # initialize the Player object
    ai = AiPlayer() # initialize the AiPlayer object

    while(game.get_state() == True): # keep looping if the game state is True
        human.set_choice() # set human choice
        
        if human.get_choice() not in game.options: # check the input and break the loop if the input is not what we want
            print('Error 1: Incorrect input')
            continue

        ai.set_choice() # set the ai choice

        print(f'{human.name} selected: {human.get_choice()}') 
        print(f'{ai.name} selected: {ai.get_choice()}')

        # compare the choices and display the winner
        print('------------------------')
        if ai.get_choice() == human.get_choice():
            print('[Draw]')

        elif ai.get_choice() == 'rock' and human.get_choice() == 'scissors':
            print(f'[{ai.name} won]')

        elif ai.get_choice() == 'paper' and human.get_choice() == 'rock':
            print(f'[{ai.name} won]')

        elif ai.get_choice() == 'scissors' and human.get_choice() == 'paper':
            print(f'[{ai.name} won]')

        else:
            print(f'[{human.name} won]')
        print('------------------------')
        
        game.sessions += 1 # track game sessions

        print(f'Total sessions ran: {game.get_sessions()}') # display total sessions ran
        
        while(True):
            exit_condition = input('Would you like to continue? y/n: ')  # get the exit condition

            if exit_condition not in ['y', 'n']:  # check the input and break the loop if it is not what we want
                print('Error 2: Incorrect input')
                continue
            else:
                break

        if exit_condition == 'n':
            game.close() # close the game

        else:
            continue

# entry point
if __name__ == '__main__':
    main()
