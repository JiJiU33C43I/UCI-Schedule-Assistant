##### HomePage.py #####
# This is a python module that creates the Homepage for UCI-Schedule-Assistant

#=======================================
#==            IMPORTS LIB            ==
#=======================================
import Pages as p
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

class HomePage(p.Pages):

    def __init__(self, MainFrame):
        super().__init__(MainFrame);  # instantiate "self.PageFrame"

        # ------ Instantiate TK VAR ------ #
        self.account_name = tk.StringVar();
        self.account_password = tk.StringVar();
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ #

        self.create_frame();
        self.layout_frame();
        self.generate_widgets();

    def create_frame(self):

        ht = (70,80,70,45,100,30,56,20,56,45,32,55,40,21); #height tuple for each frame below sequentially

        w,h = self.page_size();

        if (sum(ht) != h):
            raise self.PageHasInvalidSize("Total Frame Height(:={}) is not equal to the Root Window Height(:={})".format(sum(ht), self.page_size()["height"]));

        self.Fheader = tk.Frame(self.PageFrame, width = w, height = ht[0], bg = '#000000', padx = 10);
        self.Fblank1 = tk.Frame(self.PageFrame, width = w, height = ht[1], bg = '#ffffff');
        self.Fwelcome_banner = tk.Frame(self.PageFrame, width = w, height = ht[2], bg = '#ffffff');
        self.Fblank2 = tk.Frame(self.PageFrame, width = w, height = ht[3], bg = '#ffffff');
        self.Faccount_image = tk.Frame(self.PageFrame, width = w, height = ht[4], bg = '#ffffff', pady = 1);
        self.Fblank3 = tk.Frame(self.PageFrame, width = w,  height = ht[5], bg = '#ffffff');
        self.Faccount_name = tk.Frame(self.PageFrame, width = w,  height = ht[6], bg = '#ffffff');
        self.Fblank4 = tk.Frame(self.PageFrame, width = w,  height = ht[7], bg = '#ffffff');
        self.Faccount_password = tk.Frame(self.PageFrame, width = w,  height = ht[8], bg = '#ffffff');
        self.Fblank5 = tk.Frame(self.PageFrame, width = w,  height = ht[9], bg = '#ffffff');
        self.Fsubmit = tk.Frame(self.PageFrame, width = w,  height = ht[10], bg = '#ffffff');
        self.Fblank6 = tk.Frame(self.PageFrame, width = w,  height = ht[11], bg = '#ffffff');
        self.Ffooter = tk.Frame(self.PageFrame, width = w,  height = ht[12], bg = '#ffffff');

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

    def FHeader_widgets(self):
        self.home_image = Image.open("UCI_black_logo.PNG", mode = 'r');
        self.home_image = self.home_image.resize((267,63));
        self.home_image = ImageTk.PhotoImage(self.home_image);
        self.home_label = tk.Label(self.Fheader, image = self.home_image,
                                   bd = 0,  relief = "flat",
                                   bg = '#000000', activebackground = '#000000');
        self.home_label.pack(anchor = tk.W);

    def Fwelcome_banner_widgets(self):
        self.welcome_banner_label = tk.Label(self.Fwelcome_banner, text = "Welcome to UCI Schedule Assistant",
                                             font = font.Font(family = "Arial", size = -50),
                                             bd = 0, bg = '#ffffff');
        self.welcome_banner_label.pack();

    def Faccount_image_widgets(self):
        self.account_image = Image.open("account_image.png", mode='r');
        self.account_image = self.account_image.resize((100, 100));
        self.account_image = ImageTk.PhotoImage(self.account_image);
        self.account_image_label = tk.Label(self.Faccount_image, image = self.account_image,
                                            bd = 0,  relief = "flat",
                                            bg = '#000000', activebackground = '#000000');
        self.account_image_label.pack();

    def Faccount_name_widgets(self):
        self.account_name_label = tk.Label(self.Faccount_name, text = "Gmail Account",
                                           font = font.Font(family = "Segoe UI", size = -15),
                                           bd = 0, bg = '#ffffff');
        self.account_name_label.grid(column = 0, row = 0, sticky = tk.W, padx = (495,0));

        self.account_name.set("Please enter your gmail:")
        self.account_name_entry = tk.Entry(self.Faccount_name, textvariable = self.account_name,
                                           font = font.Font(family = "Segoe UI", size = -15),
                                           bg='#ffffff', bd = 2, width = 35, relief = tk.GROOVE);
        self.account_name_entry.grid(column = 0, row = 1, sticky = tk.W, padx = (495,0));

    def Faccount_password_widgets(self):
        self.account_password_label = tk.Label(self.Faccount_password, text = "Password",
                                               font = font.Font(family = "Segoe UI", size = -15),
                                               bd = 0, bg = '#ffffff');
        self.account_password_label.grid(column = 0, row = 0, sticky = tk.W, padx = (495,0));
        self.account_password_entry = tk.Entry(self.Faccount_password, textvariable = self.account_password,
                                               font = font.Font(family = "Segoe UI", size = -15),
                                               bg='#ffffff', bd = 2, width = 35, relief = tk.GROOVE);
        self.account_password_entry.grid(column = 0, row = 1, sticky = tk.W, padx = (495,0));

    def generate_widgets(self):
        self.FHeader_widgets();
        self.Fwelcome_banner_widgets();
        self.Faccount_image_widgets();
        self.Faccount_name_widgets();
        self.Faccount_password_widgets()






