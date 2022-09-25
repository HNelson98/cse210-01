'''
Tic-Tac-Toe
Author: Henry Nelson
'''

def main():
    current_player = "X"
    play_game(current_player)

def create_board(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

def play_game(current_player):
    game_over = False
    values = [num for num in range(1,10)]

    player_marks = {"X":[], "O":[]}

    while not game_over:

        create_board(values)

        print(current_player + "'s turn. What square are you goin in? (1-9)")
        move = int(input())

        if 1 < move > 9:
            print("Invalid Move!")
        elif values[move - 1] == "X" or values[move - 1] == "O":
            print("Already Occupied!")
        else:

            values[move - 1] = current_player

            player_marks[current_player].append(move)

            if check_winner(player_marks, current_player):
                game_over = True
                create_board(values)
                print(current_player + " has won!!")

            if check_draw(player_marks):
                game_over = True
                create_board(values)
                print("Draw Game!")


            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

def check_winner(player_marks, current_player):

    solutions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    for combinations in solutions:
        if all(marks in player_marks[current_player] for marks in combinations):
            return True

def check_draw(player_marks):
    if len(player_marks["X"]) + len(player_marks["O"]) == 9:
        return True


if __name__ == "__main__":
    main()