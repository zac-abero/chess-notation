import cv2
import time
import os
import numpy as np
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
# Load in gif "buckets" into arrays or lists to be accessed based on their assigned purpose, potentially move into a map with (K, V) key, value pairs for each piece, and centipawn assignment
gif = "gifs/SwimmingHorse.gif"
gif2 = "gifs/Soldier_Bird.gif"
gif3 = "gifs/Dancers.gif"
gif4 = "gifs/explosion-explode.gif"

gif_array = [gif, gif2, gif3, gif4]

iterate_number = 1
#def main():
while(True):

    for gif_oing in gif_array:
        reader = imageio.get_reader(gif_oing, mode='i')
        imageio.get_reader

        # speed in milliseconds
        gif_speed = 10

        # opencv create a window for viewing in live
        cv2.namedWindow("gif", cv2.WINDOW_NORMAL)

        # keypress logic, save for later
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
        #         return False  # stop listener; remove this if want more keys

            # ghetto main
            
            # listener = keyboard.Listener(on_press=on_press)
            # listener.start()  # start to listen on a separate thread
            # listener.join()  # remove if main thread is polling self.keys

        for frame in reader:

            # PREPROCESSING GIF FRAME

            # resize frame to be consisent with eachother
            frame = cv2.resize(frame, (1920, 1080))
            print(frame.shape)

            # pre process into a grayscale format
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # frame is RGB; OpenCV expects BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            
            # MANIPULATION OF GIF FRAME
             # Example manipulation

            #frame = cv2.GaussianBlur(frame, (15, 15), 0)
            #frame = cv2.medianBlur(frame, 11)
            
            # multiplication changes the value scale to be more intense
            frame = abs(frame + iterate_number)
            
            upper_bound = 50
            
            # TODO: leaving off in a spot where i can fluctuate the iterate number to "pulse" the frame's value
            
            if (iterate_number >= 0 & iterate_number <= upper_bound):
                iterate_number += 1
            elif (iterate_number >= upper_bound):
                iterate_number -= 1

            

           

            cv2.imshow("gif", frame)

            # Control playback speed (milliseconds)
            if cv2.waitKey(gif_speed) & 0xFF == ord("q"):
                break

cv2.destroyAllWindows()