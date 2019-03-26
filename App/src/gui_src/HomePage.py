##### HomePage.py #####
# This is a python module that creates the Homepage for UCI-Schedule-Assistant

#=======================================
#==            IMPORTS LIB            ==
#=======================================
import pathlib

import Pages as P
import GuiWidgets as W

from tkinter import font
from tkinter import messagebox as popmsg
import tkinter as tk
from PIL import Image, ImageTk

#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
DEBUGGING = True;
CURR_WORKING_DIR = pathlib.Path.cwd();

#=======================================
#==            Source Code            ==
#=======================================

class HomePage(P.Pages):

    def __init__(self, MainFrame, account_name, account_password):
        super().__init__(MainFrame, account_name, account_password);  # instantiate "self.PageFrame"
        self.create_frame();
        self.layout_frame();
        self.generate_widgets();

    def create_frame(self):

        ht = (70,70,70,40,100,35,56,30,56,50,32,65,46); # height tuple for each frame below sequentially

        w,h = self.page_size();

        if (sum(ht) != h):
            raise self.PageHasInvalidSize("Total Frame Height(:={}) is not equal to the Root Window Height(:={})".format(sum(ht), h));

        self.Fheader = W.Frame(self.PageFrame, w, ht[0], bg = '#000000');
        self.Fblank1 = W.Frame(self.PageFrame, w, ht[1]);
        self.Fwelcome_banner = W.Frame(self.PageFrame, w, ht[2]);
        self.Fblank2 = W.Frame(self.PageFrame, w, ht[3]);
        self.Faccount_image = W.Frame(self.PageFrame, w, ht[4]);
        self.Fblank3 = W.Frame(self.PageFrame, w,  ht[5]);
        self.Faccount_name = W.Frame(self.PageFrame, w,  ht[6]);
        self.Fblank4 = W.Frame(self.PageFrame, w,  ht[7]);
        self.Faccount_password = W.Frame(self.PageFrame, w,  ht[8]);
        self.Fblank5 = W.Frame(self.PageFrame, w,  ht[9]);
        self.Fsubmit = W.Frame(self.PageFrame, w,  ht[10]);
        self.Fblank6 = W.Frame(self.PageFrame, w,  ht[11]);
        self.Ffooter = W.Frame(self.PageFrame, w,  ht[12], bg = '#ffffff');


    def layout_frame(self):
        self.Fheader.grid(column = 0, row = 0, sticky = self.ALL_STICK);
        self.Fblank1.grid(column = 0, row = 1, sticky = self.ALL_STICK);
        self.Fwelcome_banner.grid(column = 0, row = 2, sticky = self.ALL_STICK);
        self.Fblank2.grid(column = 0, row = 3, sticky = self.ALL_STICK);
        self.Faccount_image.grid(column = 0, row = 4, sticky = self.ALL_STICK);
        self.Fblank3.grid(column = 0, row = 5, sticky = self.ALL_STICK);
        self.Faccount_name.grid(column = 0, row = 6, sticky = self.ALL_STICK);
        self.Fblank4.grid(column = 0, row = 7, sticky = self.ALL_STICK);
        self.Faccount_password.grid(column = 0, row = 8, sticky = self.ALL_STICK);
        self.Fblank5.grid(column = 0, row = 9, sticky = self.ALL_STICK);
        self.Fsubmit.grid(column = 0, row = 10, sticky = self.ALL_STICK);
        self.Fblank6.grid(column = 0, row = 11, sticky = self.ALL_STICK);
        self.Ffooter.grid(column = 0, row = 12, sticky = self.ALL_STICK);

    def Fheader_widgets(self):

        self.home_image = W.OpenImage(CURR_WORKING_DIR/"pics"/"UCI_black_logo.png");

        self.home_canvas = W.Canvas(self.Fheader, 300, 70, bg = '#000000');
        self.home_canvas.pack(anchor = tk.NW);

        self.home_canvas_img1 = self.home_canvas.create_image(16,3, image = self.home_image, anchor = tk.NW);

        def temp_func(event):
            popmsg.askyesno("Flow_Incomplete_Exception: failed to invoke JUMP to another page", "Jump to the Home Page?");

        self.home_canvas.tag_bind(self.home_canvas_img1, '<Button-1>', func = temp_func);

    def Fwelcome_banner_widgets(self):
        self.welcome_banner_label = tk.Label(self.Fwelcome_banner, text = "Welcome to UCI Schedule Assistant",
                                             font = font.Font(family = "Arial", size = -50),
                                             bd = 0, bg = '#ffffff');
        self.welcome_banner_label.pack();

    def Faccount_image_widgets(self):
        self.account_image = W.OpenImage(CURR_WORKING_DIR/"pics"/"account_image.png");
        self.account_image_label = tk.Label(self.Faccount_image, image = self.account_image,
                                            bd = 0,  relief = tk.FLAT,
                                            bg = '#ffffff', activebackground = '#ffffff');
        self.account_image_label.pack();

    def Faccount_name_widgets(self):
        self.account_name_label = tk.Label(self.Faccount_name, text = "Gmail Account",
                                           font = font.Font(family = "Segoe UI", size = -15),
                                           bd = 0, bg = '#ffffff');
        self.account_name_label.grid(column = 0, row = 0, sticky = tk.W, padx = (500,0));

        self.account_name.set("Please enter your gmail:")
        self.account_name_entry = tk.Entry(self.Faccount_name, width = 30, textvariable = self.account_name,
                                           font = font.Font(family = "Segoe UI", size = -17),
                                           bg='#ffffff', bd = 0, relief = tk.GROOVE,
                                           highlightbackground = '#666666', highlightcolor='#666666', highlightthickness = 2);
        self.account_name_entry.grid(column = 0, row = 1, sticky = tk.W, padx = (500,0), pady = (5,0));

    def Faccount_password_widgets(self):
        self.account_password_label = tk.Label(self.Faccount_password, text = "Password",
                                               font = font.Font(family = "Segoe UI", size = -15),
                                               bd = 0, bg = '#ffffff');
        self.account_password_label.grid(column = 0, row = 0, sticky = tk.W, padx = (500,0));
        self.account_password_entry = tk.Entry(self.Faccount_password, width = 30, textvariable = self.account_password,
                                               font = font.Font(family = "Segoe UI", size = -17),
                                               bg='#ffffff', bd = 0, relief = tk.GROOVE,
                                               highlightbackground='#666666', highlightcolor='#666666', highlightthickness=2,
                                               show = '*');
        self.account_password_entry.grid(column = 0, row = 1, sticky = tk.W, padx = (500,0), pady = (5,0));

    def Fsubmit_widgets(self):
        self.submit_button_image = W.OpenImage(CURR_WORKING_DIR/"pics"/"home_submit_button.png");
        self.submit_button = tk.Button(self.Fsubmit, image = self.submit_button_image,
                                       bd = 0, highlightthickness = 0);
        self.submit_button.pack(anchor = tk.W, padx = (577,0));

        def jump_to_FunctionPage(event, self = self):
            popmsg.showinfo("Account/Password capture Succeed", f"Your Gmail Account = {self.account_name.get()}\n Your Password = {self.account_password.get()}");
        self.submit_button.bind('<Button-1>', func = jump_to_FunctionPage);

    def Ffooter_widgets(self):
        self.moreinfo_button_image = W.OpenImage(CURR_WORKING_DIR/"pics"/"LearnMore_icon.png");
        self.moreinfo_button = tk.Button(self.Ffooter, image = self.moreinfo_button_image,
                                         bg = '#ffffff', pady = 9,
                                         bd = 0, highlightthickness = 0);
        self.moreinfo_button.pack(anchor = tk.E, padx = (0,6));

        def temp_func(event):
            popmsg.askyesno("Flow_Incomplete_Exception: failed to invoke JUMP to another page",
                            "Jump to the AboutUs Page?");
        self.moreinfo_button.bind('<Button-1>', func = temp_func);

    def generate_widgets(self):
        self.Fheader_widgets();
        self.Fwelcome_banner_widgets();
        self.Faccount_image_widgets();
        self.Faccount_name_widgets();
        self.Faccount_password_widgets();
        self.Fsubmit_widgets();
        self.Ffooter_widgets();






