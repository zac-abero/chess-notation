import chess.pgn
import chess.svg
import math
from stockfish import Stockfish
import gif_handler_output
from time import sleep
from pynput import keyboard #testing purposes

test = True

def main():
    # begin stockfish engine, ensure that path is correct.
    try: 
        stockfish = Stockfish(path="stockfish-windows-x86-64-avx2/stockfish/stockfish-windows-x86-64-avx2.exe", depth=15, parameters={"Threads": 2, "Minimum Thinking Time": 30})
    except Exception as e:
        print("Error loading Stockfish engine:", e)
        return
    
    # Load and open PGN file
    file = 'sample_pgns/wmeier_vs_odmitrius_2021.05.04.pgn'

    pgn = open(file)

    game = chess.pgn.read_game(pgn)
    handler = gif_handler_output.gif_handler(file)


    game.headers["Event"]
    'Live Chess'

    # Iterate through all moves and play them on a board.
    board = game.board()
    chess.svg.board(board, size=350)


    # Centipawn evaluation after each move, using Stockfish, negative meaning black is leading, positive meaning white is leading.
    # M values are for mate in x moves.

    for move in game.mainline_moves(): 
        stockfish.set_fen_position(board.fen())
        eval = stockfish.get_evaluation() 

        if test:
            print(eval)
        
        
        if eval['type'] == 'cp':
            
            if test:
                print("Centipawn evaluation: ", eval['value'])
                
            centipawn_value = eval['value']
            
            eval = handler.evaluate(centipawn_value, 0)
            handler.add_gif(eval)

            
        elif eval['type'] == 'mate':
            
            if test:
                print("Mate in ", eval['value'])

             # Example conversion for mate scores
             # If eval['value'] is positive, white is winning; if negative, black is winning.
             # Extract sign from value
             # perform mate to centipawn calculation
             # add sign back to number.
            

            centipawn_value = math.copysign(1, eval['value']) * (100 * (21 - min(10, abs(eval['value']))) )
            mate_value = eval['value']
            
            if test:
                print(centipawn_value)
            
            eval = handler.evaluate(centipawn_value, mate_value)
            handler.add_gif(eval)
        
        

        board.push(move)
        print(board)
    handler.finish()
    exit()
    
main()
