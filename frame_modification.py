import cv2

test = False

# apply some math to the frame in some way lol, maybe make a separate class?
def modify_frame():
    return

# basic frame inversion function using in-house bitwise operation
def invert_frame(frame):
    
    if test:
        print("invertframe")

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame = cv2.bitwise_not(frame)
    return frame

def xor_frame(frame, frame1):
    
    if test:
        print("overlayframe")

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame = cv2.bitwise_xor(frame, frame1)
    return frame

def overlay_frame(frame, overlay_frame):
    
    if test:
        print("overlayframe")
    return frame