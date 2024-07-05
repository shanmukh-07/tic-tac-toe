board = [' ' for x in range(10)]

def checkBoardFull(board):
    return ' ' not in board[1:]
def printBoard(board):
    # print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    # print('   |   |')
    print('-----------')
    # print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    # print('   |   |')
    print('-----------')
    # print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    # print('   |   |')
    print('-----------')


def spaceIsFree(pos):
    return board[pos] == ' '

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))


def insertLetter(letter, pos):
    board[pos] = letter

def main():
    print("Welcome to Tic Tac Toe!")
    printBoard(board)

    while not checkBoardFull(board):
        # Player's move
        playerMove()
        printBoard(board)
        if isWinner(board, 'X'):
            print("Congratulations! You win!")
            break
        if checkBoardFull(board):
            print("It's a tie!")
            break

        # Computer's move (randomly choosing an empty space)
        computerMove()
        printBoard(board)
        if isWinner(board, 'O'):
            print("Sorry, you lose!")
            break
        if checkBoardFull(board):
            print("It's a tie!")
            break

def computerMove():
    import random
    run = True
    while run:
        move = random.randint(1, 9)
        if spaceIsFree(move):
            run = False
            insertLetter('O', move)

def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Sorry, this space is occupied!")
            else:
                print("Please type a number within the range!")
        except ValueError:
            print("Please type a valid number!")

if __name__ == "__main__":
    main()
