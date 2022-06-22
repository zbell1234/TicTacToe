import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def getMove(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        spot = random.choice(game.availableMoves())
        return spot

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        valid = False
        val = None
        while not valid:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                valid = True
            except ValueError:
                print("Invalid Square, try again:")
        return val

class MiniMaxComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        if len(game.availableMoves()) == 9:
            square = random.choice(game.availableMoves()) # Randomly choose if starting
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        maxPlayer = self.letter
        otherPlayer = 'O' if player == 'X' else 'X'

        if state.currentWinner == otherPlayer:
            return {'position':None,
                    'score': 1 * (state.numEmptySquares() + 1) if otherPlayer == maxPlayer else -1 * (state.numEmptySquares() + 1)}
        elif not state.emptySquares():
            return {'position': None, 
                    'score': 0}

        if player == maxPlayer:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        
        for possibleMove in state.availableMoves():
            state.makeMove(possibleMove, player)
            simulScore = self.minimax(state, otherPlayer)
            state.board[possibleMove] = ' '
            state.currentWinner = None
            simulScore['position'] = possibleMove
            
            if player == maxPlayer:
                if simulScore['score'] > best['score']:
                    best = simulScore
            else:
                if simulScore['score'] < best['score']:
                    best = simulScore
            
        return best