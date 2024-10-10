import tkinter
import random 

ROWS = 25
COLS = 35 
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

#game window 
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

window.mainloop()