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

##### FunctionPage.py #####
# This is a python module that creates the FunctionPage for UCI-Schedule-Assistant

#=======================================
#==            IMPORTS LIB            ==
#=======================================
import pathlib
from os import sys, path
sys.path.append(path.dirname(path.dirname(__file__)))

from scrape_search_fields import scrape_fields

import Pages as P
import GuiWidgets as W


from tkinter import font
from tkinter import messagebox as popmsg
import tkinter as tk
from tkinter import ttk


#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
DEBUGGING = True;
CURR_WORKING_DIR = pathlib.Path.cwd();


#=======================================
#==            Source Code            ==
#=======================================


class FunctionPage(P.Pages):

    def __init__(self, MainFrame, account_name, account_password):
        super().__init__(MainFrame, account_name, account_password);  # instantiate PageFrame
        self.page_id = "FP";
        self.next_page_id = "FP";

        temp_search_field_engine = scrape_fields();
        temp_search_field_engine.start_to_scrape();
        self.search_fields = temp_search_field_engine.get_fields_dict();

        self.create_frame();
        self.layout_frame();
        self.generate_widgets();

    def create_frame(self):
        w,h = self.page_size();

        self.Fheader = W.Frame(self.PageFrame, w, 70, bg = '#000000');
        self.Fcurrentcourse = W.Frame(self.PageFrame, 400, 325, hlt = 1, hlb = '#888888', hlc = '#888888');
        self.Fsearchcourse = W.Frame(self.PageFrame, 400, 325, hlt = 1, hlb = '#888888', hlc = '#888888');
        self.Fdisplaypanel = W.Frame(self.PageFrame, 880, 650);

    def layout_frame(self):
        self.Fheader.grid(column = 0, row = 0, columnspan = 2);
        self.Fcurrentcourse.grid(column = 0, row = 1);
        self.Fsearchcourse.grid(column = 0, row = 2);
        self.Fdisplaypanel.grid(column = 1, row = 1, rowspan = 2);

    def Fheader_widgets(self):

        self.home_image = W.OpenImage(CURR_WORKING_DIR / "pics" / "UCI_black_logo.png");

        self.home_canvas = W.Canvas(self.Fheader, 300, 70, bg = '#000000');
        self.home_canvas.pack(anchor = tk.NW);

        self.home_canvas_img1 = self.home_canvas.create_image(16,3, image = self.home_image, anchor = tk.NW);

        def temp_func(event):
            popmsg.askyesno("Flow_Incomplete_Exception: failed to invoke JUMP to another page", "Jump to the Home Page?");

        self.home_canvas.tag_bind(self.home_canvas_img1, '<Button-1>', func = temp_func);


    def Fcurrentcourse_widgets(self):
        self.currentcourse_label = tk.Label(self.Fcurrentcourse, text = "TRACKED COURSES",
                                            font = font.Font(family = "Arial", size = -20, weight = "bold"),
                                            bg = '#ffffff', bd = 0, pady = 10);
        self.currentcourse_label.grid(row = 0, column = 0, columnspan = 3, pady = (10,0), sticky = self.ALL_STICK);



        self.trackedcourse_scrollbar = tk.Scrollbar(self.Fcurrentcourse, width = 15, orient = tk.VERTICAL);
        self.trackedcourse_panel = tk.Listbox(self.Fcurrentcourse, selectmode = tk.MULTIPLE, relief = tk.GROOVE,
                                              width = 28, bd = 2, bg = '#ffffff', highlightthickness = 0,
                                              font = font.Font(family = "Segoe UI", size = 14),
                                              yscrollcommand = self.trackedcourse_scrollbar.set);
        self.trackedcourse_scrollbar.grid(row = 1, column = 1, sticky = self.ALL_STICK);
        self.trackedcourse_panel.grid(row = 1, column = 0, sticky = self.ALL_STICK);
        self.trackedcourse_scrollbar.config(command = self.trackedcourse_panel.yview)
        for i in range(100):
            self.trackedcourse_panel.insert(tk.END, "hi");


        self.trackedcourse_control_frame = W.Frame(self.Fcurrentcourse, 90, 0, hlt = 1, hlb = '#ff0000');
        self.trackedcourse_control_frame.grid(row = 1, column = 2, sticky = self.ALL_STICK);

        self.Fcurrentcourse.columnconfigure(0, weight = 1);
        self.Fcurrentcourse.columnconfigure(1, weight = 1);
        self.Fcurrentcourse.columnconfigure(2, weight=1);
        self.Fcurrentcourse.rowconfigure(0, weight = 1);
        self.Fcurrentcourse.rowconfigure(1, weight = 1);

    def Setup_Term_Frame(self):
        self.term_label = tk.Label(self.searchcourse_term_frame, text="Term:",
                                   font=font.Font(family="Segoe UI", size=-15),
                                   bg='#ffffff');

        self.term_option_lists = tuple([ k for k in self.search_fields["YearTerm"] ]);

        self.term_curr = tk.StringVar();
        self.term_curr.set(self.term_option_lists[0]);
        self.term_option = tk.OptionMenu(self.searchcourse_term_frame, self.term_curr, *self.term_option_lists);
        #print(self.term_option.keys())
        self.term_option.configure(width=100, bg="#ffffff", relief=tk.FLAT, anchor=tk.W, padx=10,
                                   highlightthickness=2, highlightbackground="#666666", highlightcolor='#666666',
                                   font = font.Font(family="Segoe UI", size=-13) );
        self.term_label.pack(anchor=tk.NW, padx=50);
        self.term_option.pack(anchor=tk.NW, padx=50);

    def Setup_Dept_Frame(self):
        self.dept_label = tk.Label(self.searchcourse_dept_frame, text="By Department:",
                                   font=font.Font(family="Segoe UI", size=-15),
                                   bg='#ffffff');

        self.dept_option_lists = tuple([ k for k in self.search_fields["Dept"] ]);

        self.dept_curr = tk.StringVar();
        self.dept_curr.set(self.dept_option_lists[0]);
        self.dept_option = tk.OptionMenu(self.searchcourse_dept_frame, self.dept_curr, *self.dept_option_lists);
        self.dept_option.configure(width=100, bg="#ffffff", relief=tk.FLAT, anchor=tk.W, padx=10,
                                   highlightthickness=2, highlightbackground="#666666", highlightcolor='#666666',
                                   font=font.Font(family="Segoe UI", size=-13) );
        self.dept_label.pack(anchor=tk.NW, padx=50);
        self.dept_option.pack(anchor=tk.NW, padx=50);

    def Setup_Code_Frame(self):
        self.code_label = tk.Label(self.searchcourse_code_frame, text="By Course Code:",
                                   font=font.Font(family="Segoe UI", size=-15),
                                   bg='#ffffff');
        self.code_curr = tk.StringVar();
        self.code_curr.set("");
        self.code_entry = tk.Entry(self.searchcourse_code_frame, width=100, textvariable=self.code_curr,
                                   font=font.Font(family="Segoe UI", size=-15),
                                   bg='#ffffff', bd=0, relief=tk.GROOVE,
                                   highlightbackground='#666666', highlightcolor='#666666', highlightthickness=2);

        self.code_label.pack(anchor=tk.NW, padx=50);
        self.code_entry.pack(anchor=tk.NW, padx=50, ipady = 3);

    def Setup_Button_Frame(self):
        self.search_submit_img = W.OpenImage(CURR_WORKING_DIR/"pics"/"search_submit_button.png");
        self.search_submit_button = tk.Button(self.searchcourse_button_frame, image=self.search_submit_img,
                                              bd=0, highlightthickness=0);
        self.search_submit_button.pack(pady = 15);


    def Fsearchcourse_widgets(self):
        self.searchcourse_label = tk.Label(self.Fsearchcourse, text="SEARCH COURSES",
                                           font=font.Font(family="Arial", size=-20, weight="bold"),
                                           bg='#ffffff', bd=0, pady = 10);
        self.searchcourse_label.grid(row = 0, column = 0, pady = (20,0), sticky = self.ALL_STICK);


        self.searchcourse_term_frame = W.Frame(self.Fsearchcourse, 400, 70);
        self.searchcourse_term_frame.grid(row = 1, column = 0, sticky = self.ALL_STICK);
        self.Setup_Term_Frame();

        self.searchcourse_dept_frame = W.Frame(self.Fsearchcourse, 400, 70);
        self.searchcourse_dept_frame.grid(row=2, column=0, pady = 7, sticky=self.ALL_STICK);
        self.Setup_Dept_Frame();

        self.searchcourse_code_frame = W.Frame(self.Fsearchcourse, 400, 70);
        self.searchcourse_code_frame.grid(row=3, column=0, sticky=self.ALL_STICK);
        self.Setup_Code_Frame();

        self.searchcourse_button_frame = W.Frame(self.Fsearchcourse, 400, 90);
        self.searchcourse_button_frame.grid(row=4, column=0, sticky=self.ALL_STICK);
        self.Setup_Button_Frame();

        self.Fsearchcourse.columnconfigure(0, weight=1);
        self.Fsearchcourse.rowconfigure(0, weight=1);
        self.Fsearchcourse.rowconfigure(1, weight=1);
        self.Fsearchcourse.rowconfigure(2, weight=1);
        self.Fsearchcourse.rowconfigure(3, weight=1);
        self.Fsearchcourse.rowconfigure(4, weight=1);



    def Fdisplaypanel_widgets(self):
        self.display_canvas = W.Canvas(self.Fdisplaypanel, 880, 650);
        self.display_canvas.pack();
        self.idle_image = W.OpenImage(CURR_WORKING_DIR/"pics"/"MemePic.png");
        self.idle_image_canvas = self.display_canvas.create_image(0,0,anchor = tk.NW, image = self.idle_image);




    def generate_widgets(self):
        self.Fheader_widgets();
        self.Fcurrentcourse_widgets();
        self.Fsearchcourse_widgets();
        self.Fdisplaypanel_widgets();





