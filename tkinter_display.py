import tkinter as tk
import sched, time
from PIL import Image, ImageTk

#pip install pillow

running_gif = 'gifs/SwimmingHorse.gif'

class chessVisualizer(tk.Frame):
    
    def __init__(self, root):
        
        super().__init__(
            root,
            bg='BLACK'
        )
        
        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label_gif1 = tk.Label(
            self.main_frame,
            bg='BLACK',
            border=0,
            highlightthickness=0
        )
        
        self.gif1_frames = self._get_frames(running_gif)
        
        #self._play_gif(self.label_gif1, self.gif1_frames)
        
        root.after(10, self._play_gif, self.label_gif1, self.gif1_frames)
        
        
        self.label_gif1.config(
            image=self.gif1_frames[100]
        )
        
        for frame in self.gif1_frames:
            print(frame)
        
        self.label_gif1.grid(column=0, row=0)
        
    def _get_frames(self, img):
        
            with Image.open(img) as gif:
                index = 0
                frames = []
                while True:
                    try:
                        gif.seek(index)
                        frame = ImageTk.PhotoImage(gif)
                        frames.append(frame)
                    except EOFError:
                        break
                    index += 1
                return frames
            
    def _play_gif(self, label, frames):
        
        total_delay = 50
        delay_frames = 10
        
        for frame in frames:
            root.after(total_delay, self._next_frame, frame, label, frames)
            total_delay += delay_frames
        root.after(total_delay, self._next_frame, frame, label, frames)

            
    def _next_frame(self, frame, label, frames, restart=False):
        
        if restart:
            root.after(1, self._play_gif, label, frames)
            return
        else:
            self._change_gif()
        
        label.config(
            image=frame
        )
        
    def _change_gif(self):
        running_gif = 'gifs/Soldier_Bird.gif'
            
root = tk.Tk()
root.title('gifdisplay')
root.geometry('1000x1000')
root.resizable(width=False, height=False)

my_app_instance = chessVisualizer(root)

root.mainloop()