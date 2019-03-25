##### main_gui.py #####
# This is a python module that is the main module that starts the GUI for this project

#=======================================
#==            IMPORTS LIB            ==
#=======================================
import tkinter as tk;
from PIL import Image;

import GuiWidgets as W;

import HomePage;
import FunctionPage;


#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================

DEBUGGING = True;

DEFAULT_WINDOW_SIZE = (1280, 720);
START_COORDINATE = (25,25);


#=======================================
#==            Source Code            ==
#=======================================



class main_gui():
    default_win_size = DEFAULT_WINDOW_SIZE;
    default_start_coord = START_COORDINATE;

    def __init__(self, win_size = default_win_size, start_coord = default_start_coord):

        w,h = win_size;
        x,y = start_coord;

        #self.app_icon = Image.open("app_icon.ico", mode = 'r');

        # ------ DEFINING THE ROOT APP WINDOW ------ #
        self.Root = tk.Tk();
        self.Root.iconbitmap("app_icon.ico");
        self.Root.title("UCI Schedule Assistant");
        self.Root.geometry(f"{w}x{h}+{x}+{y}");
        self.Root.resizable(width = False, height = False);
        self.Root.grid_propagate(False);
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ #


        # --------- DEFINING THE MAIN FRAME --------- #
        self.MainFrame = W.Frame(self.Root, w, h);
        self.MainFrame.pack();
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ #

        # ------ Instantiate TK VAR ------ #
        self.account_name = tk.StringVar();
        self.account_password = tk.StringVar();
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ #

        # --------- Initialize the First Page --------- #
        self.CurrentPage = FunctionPage.FunctionPage(self.MainFrame, self.account_name, self.account_password);
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ #


    def run(self):
        self.Root.mainloop();



#=======================================
#==       DEBUGGING AND TESTING       ==
#=======================================

if __name__ == "__main__":
    main_gui().run();

