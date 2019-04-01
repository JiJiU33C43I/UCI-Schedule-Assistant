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

##### main_gui.py #####
# This is a python module that is the main module that starts the GUI for this project

#=======================================
#==            IMPORTS LIB            ==
#=======================================
import pathlib
from os import sys, path
sys.path.append(path.dirname(path.dirname(__file__)))

import threading
import multiprocessing

import tkinter as tk;

import GuiWidgets as W;

import HomePage;
import FunctionPage;


#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================

DEBUGGING = True;

DEFAULT_WINDOW_SIZE = (1280, 720);
START_COORDINATE = (25,25);

CURR_WORKING_DIR = pathlib.Path.cwd();

def get_current_os():
    operating_systems = {'linux1':'Linux', 'linux2':'Linux', 'darwin':'MAC OS X', 'win32':'Windows'}
    if sys.platform not in operating_systems:
        return sys.platform;
    else:
        return operating_systems[sys.platform];

CURR_OPERATING_SYSTEM = get_current_os();

#=======================================
#==            Source Code            ==
#=======================================



class main_gui():
    default_win_size = DEFAULT_WINDOW_SIZE;
    default_start_coord = START_COORDINATE;

    def __init__(self, win_size = default_win_size, start_coord = default_start_coord):

        self._running = False;

        w,h = win_size;
        x,y = start_coord;

        #self.app_icon = Image.open("app_icon.ico", mode = 'r');

        # ------ DEFINING THE ROOT APP WINDOW ------ #
        self.Root = tk.Tk();
        self.Root.iconbitmap(CURR_WORKING_DIR/"pics"/"app_icon.ico");
        self.Root.title("UCI Schedule Assistant - {} Operating System".format(CURR_OPERATING_SYSTEM));
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
        page_id = ("HP", "FP", "AB");
        self.curr_page_id = "HP";
        self.CurrentPage = HomePage.HomePage(self.MainFrame, self.account_name, self.account_password);
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ #


    def run(self):
        self._running = True;
        self.update();
        self.Root.mainloop();
        self._running = False;
        print('GUI Terminated');

    def update(self):
        self.MainFrame.update();
        self.CurrentPage.update();
        #print("Email: {}; Password: {}".format(self.account_name.get(), self.account_password.get()));
        if (self.CurrentPage.switch()):
            self.CurrentPage.destroy();
            if (self.CurrentPage.next_page_id == "HP"):
                self.CurrentPage = HomePage.HomePage(self.MainFrame, self.account_name, self.account_password);
            elif (self.CurrentPage.next_page_id == "FP"):
                self.CurrentPage = FunctionPage.FunctionPage(self.MainFrame, self.account_name, self.account_password);
        print('GUI Refresh');
        self.Root.after(250, self.update)



#=======================================
#==       DEBUGGING AND TESTING       ==
#=======================================

if __name__ == "__main__":
    App_Gui = main_gui();
    App_Gui.run();


