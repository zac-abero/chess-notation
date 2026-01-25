import chess.pgn
import chess.svg
import stockfish
from time import sleep
from pynput import keyboard #testing purposes



def main():

    file = 'sample_pgns/vvurst_vs_saiyam000_2025.11.10.pgn'

    pgn = open(file)

    first_game = chess.pgn.read_game(pgn) 

    first_game.headers["Event"]
    'Live Chess'

    # Iterate through all moves and play them on a board.
    board = first_game.board()
    chess.svg.board(board, size=350)


    for move in first_game.mainline_moves(): 
        board.push(move)
        print(board)


#  # keypress logic, save for later
# def on_press(key):
#     if key == keyboard.Key.esc:
#         return False  # stop listener
#     try:
#         k = key.char  # single-char keys
#     except:
#         k = key.name  # other keys
#     if k in ['space', 'up', 'down']:  # keys of interest
#         # self.keys.append(k)  # store it in global-like variable
#         print('Key pressed: ' + k)
#         return True
 
# # Run the main function            
main()
