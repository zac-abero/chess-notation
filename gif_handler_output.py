import cv2
import pprint
import time
import os
import math
import numpy as np
import imageio
import frame_modification as fm
from random import random
from pynput import keyboard #testing purposes

'''TODO: 
- Load in gif "buckets (centipawn 0-10)" into arrays or lists to be accessed
- Thread a listener to interrupt for testing purposes to help with transitions (testing for live view)
- develop a function to apply an image manipulation over an entire gif (iterate through gif)
- run a couple functions on each gif ahead of time, but run a check first if the gif is pre filtered (hopefully gifs come sized correctly)
- 
'''
# Load in gif "buckets" into arrays or lists to be accessed based on their assigned purpose, 
# potentially move into a map with (K, V) key, value pairs for each piece, and centipawn assignment

# Load in gif "buckets" into arrays or lists to be accessed based on their assigned purpose, 
# each bucket corresponds to a centipawn loss range 

# create a mode switch between live view and export, live view constantly loops until new information is acquired to change the gif, export is to create a video or gif set of a chess pgn

mode = "export"

test = True

# speed in milliseconds
gif_fps = 10

## Global Variables ##

# relative path to folders 
path = 'gifs\organized'
# list of paths to gif bucket folders
path_list = []
# output path
output_path = 'gifs\output_gifs'

# gif paths sorted into each category, or "bucket" 1-5, 9 saved for mate docs for now
buckets = {1: [], 2: [], 3: [], 4: [], 5: [], 9: []}
# placeholder
files = []
# output
final_gif = []
# pgn name to be appended for output reasons
pgn_filename = ''

# toggle variable to tell main() to stop adding
game_over = False


iterate_number = 1

class gif_handler:
    def __init__(self, pgn):
        self.pgn = pgn
        #self.buckets = []
        # fetch all gif paths and organize into buckets
        try:
                print(os.listdir(path))
                bucket_list = os.listdir(path)
                # fetch path list for each bucket
                path_list = [x[0] for x in os.walk(path)]
                
                if test:
                    print(path_list)

                # iterate through each bucket path and sort gifs into their respective lists
                for p in path_list:
                    for f in os.listdir(p):
                        for i in bucket_list:
                            if f.endswith('.gif') and i in p:
                                buckets[int(i)].append(os.path.join(p, f))
                pprint.pp(buckets)
        except OSError as e:
                print("Error:", e)

        '''for i in buckets:
            for j, gif in enumerate(buckets[i]):
                reader = imageio.get_reader(gif, mode='i')
                imageio.get_reader

                # opencv create a window for viewing in live
                #cv2.namedWindow("gif", cv2.WINDOW_NORMAL)
                
                # breaking i (index of frame) and frame object into separate objects to be operated on
                for k, frame in enumerate(reader):

                    # PREPROCESSING GIF FRAME

                    # resize frame to be consisent with eachother
                    frame = cv2.resize(frame, (1280, 720))

                    # pre process into a grayscale format
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    
                    final_gif.append(frame)'''

            # gif, gif list
    def add_gif(self, eval):
        
            for j, gif in enumerate(buckets[1]):
                reader = imageio.get_reader(gif, mode='i')
                imageio.get_reader

                # opencv create a window for viewing in live
                #cv2.namedWindow("gif", cv2.WINDOW_NORMAL)
                
                # breaking i (index of frame) and frame object into separate objects to be operated on
                for k, frame in enumerate(reader):

                    # PREPROCESSING GIF FRAME

                    # resize frame to be consisent with eachother
                    frame = cv2.resize(frame, (1280, 720))

                    # pre process into a grayscale format
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    
                    final_gif.append(frame)
            return

    # swap gif from what is running, take in centipawns as a factor
    def change_gif(gif, transition_type, cp):
        return

    def transition_gif(gif, gif1, transition):
        return

    def evaluate(self, cp, mate_value):
        evaluation = 0
        if mate_value == 0:
            # ignore mate value, perform regular operation
            if test:
                print("regular move, cp: " + str(cp))
            
            cp_sign = math.copysign(1, cp)

            
            if test:
                print("cp sign" + str(cp_sign))

            # fetch the absolute value of the centipawn val
            cp = abs(cp)
            match cp:
                case cp if cp >= 600:
                    if test:
                        print("centipawns over 600")
                    evaluation = 5
                    
                case cp if cp >= 500:
                    if test:
                        print("centipawns over 500")
                    evaluation = 5
                    
                case cp if cp >= 400:
                    if test:
                        print("centipawns over 400")
                    evaluation = 4
                    
                case cp if cp >= 300:
                    if test:
                        print("centipawns over 300")
                    evaluation = 3
                    
                case cp if cp >= 200:
                    if test:
                        print("centipawns over 200")
                    evaluation = 2
                    
                case cp if cp >= 100:
                    if test:       
                        print("cenipawns over 100")
                    evaluation = 1
            
        elif mate_value >= 0 :
            if test:
                print("mate in: " + str(mate_value)) 
            match mate_value:
                case mate_value if abs(mate_value) <= 1:
                    if test:
                        print("mate in one")
                    evaluation = 9
                    return
                
        
        
                
        '''
        takes in centipawn
        
        returns an update to the gif sequence with a new gif
        '''
        return evaluation

    def finish(self):
        game_over = True
        
        final_path = os.path.join(output_path, "output.gif")   
        imageio.mimsave(final_path, final_gif, 'GIF', fps=gif_fps, loop=0)
        return

    
    
if __name__ == '__main__':
    gif_handler('sample_pgns/wmeier_vs_odmitrius_2021.05.04.pgn')