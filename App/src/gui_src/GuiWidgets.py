'''
MIT License

Copyright (c) 2019 JiJiU33C43I Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

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
                 pp = False, gp = False, sr = (0,0,0,0)):
        super().__init__(parent, width = w, height = h, relief = relief,
                         bd = bd, bg = bg, highlightbackground = hlb, highlightcolor = hlc, highlightthickness = hlt,
                         scrollregion = sr);
        self.pack_propagate(pp);
        self.grid_propagate(gp);


def OpenImage(img_path:str):
    img = Image.open(img_path, mode = 'r');
    return ImageTk.PhotoImage(img);
