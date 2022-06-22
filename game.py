from player import HumanPlayer, RandomComputerPlayer, MiniMaxComputer
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.currentWinner = None
    
    def printBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' | ')

    @staticmethod
    def printBoardNums():
        numBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numBoard:
            print(' | ' + ' | '.join(row) + ' | ')

    def availableMoves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        #return indices that have a space (not x or o)

    def emptySquares(self):
        return ' ' in self.board
    
    def numEmptySquares(self):
        return self.board.count(' ')
    
    def makeMove(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #check Row
        rowIndex = square // 3
        row = self.board[rowIndex*3 : (rowIndex + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #check Column
        columnIndex = square % 3
        column = [self.board[columnIndex + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #Check Diagonals
        if square % 2 == 0:
            diagonalLtoR = [self.board[i] for i in [0,4,8]]
            diagonalRtoL = [self.board[i] for i in [2,4,6]]

            if all(spot == letter for spot in diagonalLtoR):
                return True
            if all(spot == letter for spot in diagonalRtoL):
                return True

        return False



def play(game, xPlayer, oPlayer, printGame=True):
    if printGame:
        game.printBoardNums()

    letter = random.choice(['X','O'])

    while game.emptySquares():
        square = oPlayer.getMove(game) if letter == 'O' else  xPlayer.getMove(game)

        if game.makeMove(square, letter):
            if printGame:
                print(letter + f' makes a move to square {square}')
                game.printBoard()
                print('')

            if game.currentWinner:
                if printGame:
                    print(letter + ' wins!')
                return letter


            letter = 'O' if letter == 'X' else 'X'

    if printGame:
        print('It\'s a tie...')

if __name__ == '__main__':
    xWins = 0
    oWins = 0
    ties = 0
    xPlayer = MiniMaxComputer('X')
    oPlayer = MiniMaxComputer('O')
    
    for i in range(1000):
        t = TicTacToe()
        result = play(t, xPlayer, oPlayer, printGame=False)
        if result == 'X':
            xWins += 1
        elif result == 'O':
            oWins += 1
        else:
            ties += 1
        print(f"Completed game {i}")
    
    print(f'After 1k games, X has won {xWins} times, O has won {oWins} times, and there have been {ties} ties')