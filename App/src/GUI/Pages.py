##### Pages.py #####
# This is a python module that declares the base class <Pages>

#=======================================
#==            IMPORTS LIB            ==
#=======================================
import tkinter as tk
import GuiWidgets as W;

#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
DEBUGGING = True;

#=======================================
#==            Source Code            ==
#=======================================


class Pages:

    class PageHasInvalidSize(Exception):
        pass;

    ALL_STICK = tk.N + tk.S + tk.W + tk.E;

    def __init__(self, MainFrame):
        self.MainFrame = MainFrame;
        w,h = self.page_size();
        self.PageFrame = W.Frame(self.MainFrame, w, h);
        self.PageFrame.pack();

    def page_size(self) -> tuple:
        return ( self.MainFrame.cget("width") , self.MainFrame.cget("height") );

    def update(self):
        self.PageFrame.update();

    def destroy(self):
        self.PageFrame.destroy();