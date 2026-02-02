import cv2
import pprint
import time
import os
import numpy as np
import pandas as pd
import imageio
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


## Global Variables ##

# relative path to folders 
path = 'gifs\organized'
# list of paths to gif bucket folders
path_list = []
# gif paths sorted into each category, or "bucket" 1-5 
buckets = {1: [], 2: [], 3: [], 4: [], 5: [], 9: []}
# placeholder
files = []
# speed in milliseconds
gif_speed = 1

iterate_number = 1

# function to gain all gif paths and organize into their respective buckets
def populate_buckets():
    try:
        print(os.listdir(path))
        bucket_list = os.listdir(path)
        # fetch path list for each bucket
        path_list = [x[0] for x in os.walk(path)]
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

# this might just be change gif
def update_gif():
    return

# swap gif from what is running, take in centipawns as a factor
def change_gif(cp):
    return

# apply some math to the frame in some way lol, maybe make a separate class?
def modify_frame():
    return

def blend_frame(frame, frame1):
    frame = cv2.addWeighted(frame, 0.7, frame1, 0.3, 0)
    return frame

def flip_frame_horizontal(frame):
    
    return frame

def main():

    # fetch all gif paths and organize into buckets
    populate_buckets()
    while(True):
        for i in buckets:
            for gif in buckets[i]:
                reader = imageio.get_reader(gif, mode='i')
                imageio.get_reader

                # opencv create a window for viewing in live
                cv2.namedWindow("gif", cv2.WINDOW_NORMAL)

                for x, frame in enumerate(reader):

                    # PREPROCESSING GIF FRAME

                    # resize frame to be consisent with eachother
                    frame = cv2.resize(frame, (1920, 1080))
                    print(frame.shape)

                    # pre process into a grayscale format
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    
                    # frame is RGB; OpenCV expects BGR
                    #frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                    
                    frame = blend_frame(frame, frame)
                    # MANIPULATION OF GIF FRAME
                    # Example manipulation

                    frame = cv2.GaussianBlur(frame, (15, 15), 0)
                    #frame = cv2.medianBlur(frame, 11)
                    
                    
                    #upper_bound = 50
                    
                    # TODO: leaving off in a spot where i can fluctuate the iterate number to "pulse" the frame's value
                    
                    # if (iterate_number >= 0 & iterate_number <= upper_bound):
                    #     iterate_number += 1
                    # elif (iterate_number >= upper_bound):
                    #     iterate_number -= 1

            

                

                    cv2.imshow("gif", frame)

                    # Control playback speed (milliseconds)
                    if cv2.waitKey(gif_speed) & 0xFF == ord("q"):
                        break

        cv2.destroyAllWindows()

main()