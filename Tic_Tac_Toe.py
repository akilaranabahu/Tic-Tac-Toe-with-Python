from IPython.display import clear_output
import random


def set_array():
    x = []
    for i in range(0, 10):
        x.append(i)
    return x


game_players = [0, 'X', 'O']

availability = set_array()

Play_board = [' '] * 10


def draw_board(a, b):
    print(
        f'Available   TIC-TAC-TOE\n  moves\n\n  {a[7]}|{a[8]}|{a[9]}        {b[7]}|{b[8]}|{b[9]}\n  -----        -----\n  {a[4]}|{a[5]}|{a[6]}        {b[4]}|{b[5]}|{b[6]}\n  ------        -----\n  {a[1]}|{a[2]}|{a[3]}        {b[1]}|{b[2]}|{b[3]}\n')


draw_board(availability, Play_board)


def got_place(game_board, avai, state, sign):
    game_board[state] = sign
    avai[state] = ' '


def check_for_win(win_sign, game_board):
    return ((game_board[7] == game_board[4] == game_board[1] == win_sign) or

            (game_board[9] == game_board[6] == game_board[3] == win_sign) or

            (game_board[8] == game_board[5] == game_board[2] == win_sign) or

            (game_board[7] == game_board[8] == game_board[9] == win_sign) or

            (game_board[4] == game_board[5] == game_board[6] == win_sign) or

            (game_board[1] == game_board[2] == game_board[3] == win_sign) or

            (game_board[9] == game_board[5] == game_board[1] == win_sign) or

            (game_board[7] == game_board[5] == game_board[3] == win_sign))


def take_player():
    return random.choice((-1, 1))


def mix_player():
    change_player = take_player()
    player = game_players[change_player]
    return player, change_player


def space_availability(game_board, state):
    return game_board[state] == ' '


def board_availability(game_board):
    return ' ' not in game_board[1:]


def Set_for_run():
    draw_board(availability, Play_board)
    state = player_move(Play_board, player)
    got_place(Play_board, availability, state, player)


def draw_game():
    draw_board(availability, Play_board)
    print('The game is draw!')


def win_game():
    draw_board(availability, Play_board)
    print('Congratulations Player ' + player + ' wins!')


def continue_game(change_player):
    Some_player = game_players[change_player]
    clear_output()
    return Some_player


def player_move(game_board, player):
    state = 0

    while state not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_availability(game_board, state):
        try:
            choose_space = (input('Player %s, choose your next position: (1-9) ' % (player)))
            state = int(choose_space)


        except:
            print("please try again.")
    return state


def play_again():
    return input('Do you want to play again? Enter yes or No: ').lower().startswith('y')


while True:
    clear_output()
    print('Welcome to Tic Tac Toe')
    player, change_player = mix_player()

    print('For this round,Player %s will go first!' % (player))

    game_start = True
    input('Hit Enter to continue')
    while game_start:
        Set_for_run()

        if check_for_win(player, Play_board):
            win_game()
            game_start = False

        else:
            if board_availability(Play_board):
                draw_game()
                break
            else:
                change_player *= -1
                player = continue_game(change_player)

    Play_board = [' '] * 10
    availability = set_array()

    if not play_again():
        break
































