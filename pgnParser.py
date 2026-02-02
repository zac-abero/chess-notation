import chess.pgn
import chess.svg
import math
from stockfish import Stockfish
import gif_handler
from time import sleep
from pynput import keyboard #testing purposes



def main():
    # begin stockfish engine, ensure that path is correct.
    try: 
        stockfish = Stockfish(path="stockfish-windows-x86-64-avx2/stockfish/stockfish-windows-x86-64-avx2.exe", depth=15, parameters={"Threads": 2, "Minimum Thinking Time": 30})
    except Exception as e:
        print("Error loading Stockfish engine:", e)
        return
    
    # Load and open PGN file
    file = 'sample_pgns/11batista11_vs_vvurst_2026.01.25.pgn'

    pgn = open(file)

    first_game = chess.pgn.read_game(pgn)

    first_game.headers["Event"]
    'Live Chess'

    # Iterate through all moves and play them on a board.
    board = first_game.board()
    chess.svg.board(board, size=350)


    # Centipawn evaluation after each move, using Stockfish, negative meaning black is leading, positive meaning white is leading.
    # M values are for mate in x moves.

    for move in first_game.mainline_moves(): 
        stockfish.set_fen_position(board.fen())
        eval = stockfish.get_evaluation() 

        print(eval)
        
        if eval['type'] == 'cp':
            print("Centipawn evaluation: ", eval['value'])
        elif eval['type'] == 'mate':
            print("Mate in ", eval['value'])

             # Example conversion for mate scores
             # If eval['value'] is positive, white is winning; if negative, black is winning.
             # Extract sign from value
             # perform mate to centipawn calculation
             # add sign back to number.

            centipawn_value = math.copysign(1, eval['value']) * (100 * (21 - min(10, abs(eval['value']))) )
            print(centipawn_value)

        # if evaluation is above (lets say, abs 1900, translate to mate sequence, take sign into account)

        # TODO: add function that builds gif based on cp score and 
        # sleep timer to see it run a little slower
        # sleep(1)
        board.push(move)
        print(board)


main()
