import chess.pgn
import chess.svg
from time import sleep

file = 'sample_pgns/vvurst_vs_saiyam000_2025.11.10.pgn'

pgn = open(file)

first_game = chess.pgn.read_game(pgn)
second_game = chess.pgn.read_game(pgn)

first_game.headers["Event"]
'Live Chess'


# Iterate through all moves and play them on a board.
board = first_game.board()
chess.svg.board(board, size=350)
for move in first_game.mainline_moves():
    
    board.push(move)
    print(board)
