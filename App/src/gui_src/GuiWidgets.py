##### HomePage.py #####
# This is a python module that declares general purpose tkinter widgets and adapts it specifically for this project

#=======================================
#==            IMPORTS LIB            ==
#=======================================
from tkinter import font
import tkinter as tk
from PIL import Image, ImageTk

#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
DEBUGGING = True;

#=======================================
#==            Source Code            ==
#=======================================


class Frame(tk.Frame):

    def __init__(self, parent, w, h, padx = 0, pady = 0, relief = tk.FLAT,
                 bd = 0, bg = "#ffffff", hlb = "#ffffff", hlc = "#ffffff", hlt = 0,
                 pp = False, gp = False):
        super().__init__(parent, width = w, height = h, padx = padx, pady = pady, relief = relief,
                         bd = bd, bg = bg, highlightbackground = hlb, highlightcolor = hlc, highlightthickness = hlt);
        self.pack_propagate(pp);
        self.grid_propagate(gp);


class Canvas(tk.Canvas):
    def __init__(self, parent, w, h, relief = tk.FLAT,
                 bd = 0, bg = "#ffffff", hlb = "#ffffff", hlc = "#ffffff", hlt = 0,
                 pp = False, gp = False):
        super().__init__(parent, width = w, height = h, relief = relief,
                         bd = bd, bg = bg, highlightbackground = hlb, highlightcolor = hlc, highlightthickness = hlt);
        self.pack_propagate(pp);
        self.grid_propagate(gp);


def OpenImage(img_path:str):
    img = Image.open(img_path, mode = 'r');
    return ImageTk.PhotoImage(img);
