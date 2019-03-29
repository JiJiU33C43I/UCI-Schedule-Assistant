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

def get_current_os():
    operating_systems = {'linux1':'Linux', 'linux2':'Linux', 'darwin':'OS X', 'win32':'Windows'}
    if sys.platform not in operating_systems:
        return sys.platform;
    else:
        return operating_systems[sys.platform];

CURR_OPERATING_SYSTEM = get_current_os();


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

        self.tracked_courses = dict();
        self.display_tracked_course = tk.StringVar();

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

    def update(self):
        super().update();
        self.refresh_tracked_courses(self.trackedcourse_panel);

    def get_tracked_courses(self) -> set:
        #print(self.display_tracked_course.get());
        display_str = self.display_tracked_course.get().replace("'", " ").replace('"', " ").replace("(", " ").replace(")", " ").replace(",", " ");
        displaying_list = display_str.split();
        #print(displaying_list)
        print(set([s for s in displaying_list if (displaying_list.index(s)%5==0)]));
        return set([s for s in displaying_list if (displaying_list.index(s)%5==0)]);

    def refresh_tracked_courses(self, display_widgets):
        if (self.get_tracked_courses() != set([course_description for course_description in self.tracked_courses])):
            display_widgets.delete(0, display_widgets.size()-1);
            for course_description, course_obj in self.tracked_courses.items():
                cn, fn = course_obj.name();
                display_widgets.insert(tk.END,f"{course_description} {cn} {course_obj.type()} {course_obj.day()} {course_obj.hour()}");

    def refresh_display_panel_to_show_meme(self):
        self.Fdisplaypanel.destroy();
        self.Fdisplaypanel = W.Frame(self.PageFrame, 880, 650);
        self.Fdisplaypanel.grid(column=1, row=1, rowspan=2);
        self.display_canvas = W.Canvas(self.Fdisplaypanel, 880, 650);
        self.display_canvas.pack();
        self.idle_image = W.OpenImage(CURR_WORKING_DIR / "pics" / "MemePic.png");
        self.idle_image_canvas = self.display_canvas.create_image(0, 0, anchor=tk.NW, image=self.idle_image);

    def _scroll_canvas(self, event):
        self.display_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units");


    def return_add_tracked_course_function(self, course):
        def add_tracked_course(event):
            current_canvas_button = event.widget.find_withtag("current");
            event.widget.delete(current_canvas_button);
            self.tracked_courses[course.description()] = course;
        return add_tracked_course;




    def return_display_one_course_function(self, course):
        def display_class_info_on_canvas(derived_class, curr_x, curr_y, course_info_indent):
            course_info_font = font.Font(family="Segoe UI", size=15);
            curr_course_code = self.display_canvas.create_text(curr_x + course_info_indent[0], curr_y,
                                                               text=f"{derived_class.coursecode()}",
                                                               font=course_info_font,
                                                               anchor = tk.W);
            curr_course_type = self.display_canvas.create_text(curr_x + course_info_indent[1], curr_y,
                                                               text=f"{derived_class.type()}",
                                                               font=course_info_font,
                                                               anchor = tk.W);
            curr_course_section = self.display_canvas.create_text(curr_x + course_info_indent[2], curr_y,
                                                                  text=f"{derived_class.section()}",
                                                                  font=course_info_font,
                                                                  anchor = tk.W);
            curr_course_day = self.display_canvas.create_text(curr_x + course_info_indent[3], curr_y,
                                                              text=f"{derived_class.day()}",
                                                              font=course_info_font,
                                                              anchor = tk.W);
            curr_course_hour = self.display_canvas.create_text(curr_x + course_info_indent[4], curr_y,
                                                               text=f"{derived_class.hour()}",
                                                               font=course_info_font,
                                                               anchor = tk.W);

            curr_enr = derived_class.enr();
            curr_max = derived_class.max();
            curr_progress_percentage = tk.DoubleVar();
            curr_progress_percentage.set((curr_enr/curr_max)*100 if (curr_enr <= curr_max and curr_max != 0) else 100);

            full_progressbar_style = ttk.Style();
            full_progressbar_style.theme_use('alt')
            full_progressbar_style.map("Full.Horizontal.TProgressbar",
                                       bordercolor = [('disabled', '#ff0000')],
                                       background =  [('disabled', '#ff0000')],
                                       troughcolor =  [('disabled', '#ffffff')],
                                       thickness = [('disabled', 13)],
                                       borderwidth = [('disabled', 0)]);
            open_progressbar_style = ttk.Style();
            open_progressbar_style.theme_use('alt')
            open_progressbar_style.map("Open.Horizontal.TProgressbar",
                                       bordercolor=[('disabled', '#15AC0A')],
                                       background=[('disabled', '#15AC0A')],
                                       troughcolor=[('disabled', '#ffffff')],
                                       thickness = [('disabled', 13)],
                                       borderwidth = [('disabled', 0)]);
            wait_progressbar_style = ttk.Style();
            wait_progressbar_style.theme_use('alt')
            wait_progressbar_style.map("Wait.Horizontal.TProgressbar",
                                       bordercolor=[('disabled', '#FF9200')],
                                       background=[('disabled', '#FF9200')],
                                       troughcolor=[('disabled', '#ffffff')],
                                       thickness = [('disabled', 13)],
                                       borderwidth = [('disabled', 0)]);
            newonly_progressbar_style = ttk.Style();
            newonly_progressbar_style.theme_use('alt')
            newonly_progressbar_style.map("NewOnly.Horizontal.TProgressbar",
                                          bordercolor=[('disabled', '#00BBFF')],
                                          background=[('disabled', '#00BBFF')],
                                          troughcolor=[('disabled', '#ffffff')],
                                          thickness = [('disabled', 13)],
                                          borderwidth = [('disabled', 0)]);
            #print(full_progressbar_style.layout('Full.Horizontal.TProgressbar'))
            #print(full_progressbar_style.element_options("Horizontal.Progressbar.trough"))
            #print(full_progressbar_style.element_options("Horizontal.Progressbar.pbar"))

            if (derived_class.status() == "FULL"):
                curr_style = "Full.Horizontal.TProgressbar";
            elif (derived_class.status() == "WAITL"):
                curr_style = "Wait.Horizontal.TProgressbar";
            elif (derived_class.status() == "OPEN"):
                curr_style = "Open.Horizontal.TProgressbar";
            elif (derived_class.status() == "NEWONLY"):
                curr_style = "NewOnly.Horizontal.TProgressbar";


            curr_progress_bar = ttk.Progressbar(self.display_canvas, style = curr_style,
                                                length=200, mode='determinate', orient=tk.HORIZONTAL,
                                                variable = curr_progress_percentage);
            curr_progress_bar.place(x = curr_x + course_info_indent[5], y = curr_y+3, anchor = tk.W);
            progress_bar_window = self.display_canvas.create_window(curr_x + course_info_indent[5], curr_y + 3,
                                                                    window= curr_progress_bar);
            #curr_progress_bar.start();

            if (derived_class.status() == "FULL"):
                curr_status_info = self.display_canvas.create_text(curr_x + course_info_indent[6], curr_y,
                                                                   text="[Full]",
                                                                   font=course_info_font,
                                                                   anchor = tk.W);
            elif (derived_class.status() == "WAITL"):
                curr_status_info = self.display_canvas.create_text(curr_x + course_info_indent[6], curr_y,
                                                                   text="[WaitList : {}]".format(derived_class.wl()),
                                                                   font=course_info_font,
                                                                   anchor = tk.W);
            elif (derived_class.status() == "NEWONLY"):
                curr_status_info = self.display_canvas.create_text(curr_x + course_info_indent[6], curr_y,
                                                                   text="[NewOnly]",
                                                                   font=course_info_font,
                                                                   anchor = tk.W);


        def refresh_display_panel_to_show_one_course(event):
            self.Fdisplaypanel.destroy();
            self.Fdisplaypanel = W.Frame(self.PageFrame, 880, 650);
            self.Fdisplaypanel.grid(column=1, row=1, rowspan=2);
            self.display_canvas = W.Canvas(self.Fdisplaypanel, 860, 650, bg='#ffffff');
            self.display_scroll = tk.Scrollbar(self.Fdisplaypanel, width=20, orient=tk.VERTICAL)
            self.display_scroll.config(command=self.display_canvas.yview)
            self.display_scroll.grid(row=0, column=1, sticky=self.ALL_STICK);
            self.display_canvas.config(yscrollcommand=self.display_scroll.set);
            self.display_canvas.grid(row=0, column=0, sticky=self.ALL_STICK);
            self.Fdisplaypanel.bind_all("<MouseWheel>", self._scroll_canvas);

            cn, fn = course.name();
            curr_x,curr_y = (80,30);
            self.display_canvas.create_text(curr_x, curr_y, text = cn,
                                            font = font.Font(family = "Arial", size = 17),
                                            anchor = tk.W);
            self.display_canvas.create_text(curr_x+170, curr_y, text=fn,
                                            font=font.Font(family="Arial", size=17, weight = "bold"),
                                            anchor = tk.W);

            self.add_button_img = W.OpenImage(CURR_WORKING_DIR / "pics" / "add_button.png");

            curr_x,curr_y = (50, 80);
            indented_width = 50;
            next_increment_height = 50;
            course_info_indent = (40,110,160,210,270,500,620);

            for primary_course in course:
                if primary_course.description() not in self.tracked_courses:
                    curr_add_button = self.display_canvas.create_image(curr_x, curr_y, image=self.add_button_img);
                    self.display_canvas.tag_bind(curr_add_button, '<Button-1>', func = self.return_add_tracked_course_function(primary_course));
                display_class_info_on_canvas(primary_course, curr_x, curr_y-1, course_info_indent);
                curr_y += next_increment_height;
                for secondary_course in primary_course:
                    if secondary_course.description() not in self.tracked_courses:
                        curr_add_button = self.display_canvas.create_image(curr_x+indented_width, curr_y, image=self.add_button_img);
                        self.display_canvas.tag_bind(curr_add_button, '<Button-1>', func=self.return_add_tracked_course_function(secondary_course));
                    display_class_info_on_canvas(secondary_course, curr_x+indented_width, curr_y-1, course_info_indent);
                    curr_y += next_increment_height;

            #print(curr_y)

            self.display_canvas.config(scrollregion=(0, 0, 860, (curr_y if curr_y >= 650 else 650)));



        return refresh_display_panel_to_show_one_course;


    def refresh_display_panel_to_show_courses(self):
        self.Fdisplaypanel.destroy();
        self.Fdisplaypanel = W.Frame(self.PageFrame, 880, 650);
        self.Fdisplaypanel.grid(column=1, row=1, rowspan=2);
        self.display_canvas = W.Canvas(self.Fdisplaypanel, 860, 650, bg = '#BEF7A6');
        self.display_scroll = tk.Scrollbar(self.Fdisplaypanel, width = 20, orient = tk.VERTICAL)
        self.display_scroll.config(command = self.display_canvas.yview)
        self.display_scroll.grid(row = 0, column = 1, sticky = self.ALL_STICK);
        self.display_canvas.config(yscrollcommand = self.display_scroll.set);
        self.display_canvas.grid(row=0, column=0, sticky=self.ALL_STICK);
        self.Fdisplaypanel.bind_all("<MouseWheel>", self._scroll_canvas);

        curr_x, curr_y, w_rect, h_rect = (0,0,860,50);
        bright_color = True;

        self.clickable_rect = [];

        for course in self.CD:
            coursename, formalname = course.name();
            curr_rect = self.display_canvas.create_rectangle(curr_x, curr_y, curr_x + w_rect, curr_y + h_rect,
                                                             fill = ("#C9C9C9" if bright_color else "#FFFFFF"));
            self.clickable_rect.append(curr_rect);
            self.display_canvas.tag_bind(curr_rect, '<Button-1>', func = self.return_display_one_course_function(course));

            curr_coursename = self.display_canvas.create_text(curr_x + 20, curr_y+h_rect/2,
                                                              font = font.Font(family = "Arial", size = 14),
                                                              anchor = tk.W, text = coursename);
            curr_formalname = self.display_canvas.create_text(curr_x + 175, curr_y + h_rect / 2,
                                                              font=font.Font(family="Arial", size=14, weight = "bold"),
                                                              anchor=tk.W, text=formalname);
            curr_y += h_rect;
            bright_color = not bright_color;



        self.display_canvas.config(scrollregion=(0,0,860,(curr_y if curr_y >= 650 else 650)));

        def detect_clickable_in_canvas(event, self=self):
            clickable_bbox_list = [ self.display_canvas.bbox(clickable) for clickable in self.clickable_rect ];
            for x1, y1, x2, y2 in clickable_bbox_list:
                if (x1 <= event.x <= x2) and (y1 <= event.y <= y2):
                    self.display_canvas.config(cursor = 'hand2');
                    #print('hand2')
                    return;
            self.display_canvas.config(cursor = 'arrow');

        self.display_canvas.bind("<Motion>", detect_clickable_in_canvas)


    def Fheader_widgets(self):

        self.home_image = W.OpenImage(CURR_WORKING_DIR / "pics" / "UCI_black_logo.png");

        self.home_canvas = W.Canvas(self.Fheader, 300, 70, bg = '#000000');
        self.home_canvas.pack(anchor = tk.NW);

        self.home_canvas_img1 = self.home_canvas.create_image(16,3, image = self.home_image, anchor = tk.NW);

        def temp_func(event):
            popmsg.askyesno("Flow_Incomplete_Exception: failed to invoke JUMP to another page", "Jump to the Home Page?");

        self.home_canvas.tag_bind(self.home_canvas_img1, '<Button-1>', func = temp_func);

    def reset_tracked_courses(self,event):
        self.tracked_courses = dict();

    def delete_selected_tracked_courses(self,event):
        for line in range(self.trackedcourse_panel.size()):
            #print(line)
            if (self.trackedcourse_panel.selection_includes(line)):
                #print(self.trackedcourse_panel.get(line))
                display_str = self.trackedcourse_panel.get(line).replace("'", " ").replace('"', " ").replace("(", " ").replace(")", " ").replace(",", " ");
                displaying_list = display_str.split();
                selected_course_description = displaying_list[0];
                del self.tracked_courses[selected_course_description];


    def Fcurrentcourse_widgets(self):
        self.currentcourse_label = tk.Label(self.Fcurrentcourse, text = "TRACKED COURSES", height = 3,
                                            font = font.Font(family = "Arial", size = -20, weight = "bold"),
                                            bg = '#ffffff', bd = 0, pady = 10);
        self.currentcourse_label.grid(row = 0, column = 0, columnspan = 3, pady = (10,0), sticky = self.ALL_STICK);



        self.trackedcourse_vertical_scrollbar = tk.Scrollbar(self.Fcurrentcourse, width = 15, orient = tk.VERTICAL);
        self.trackedcourse_horizontal_scrollbar = tk.Scrollbar(self.Fcurrentcourse, width = 15, orient = tk.HORIZONTAL);
        self.trackedcourse_panel = tk.Listbox(self.Fcurrentcourse, selectmode = tk.MULTIPLE, relief = tk.GROOVE,
                                              width = 28, bd = 2, bg = '#ffffff', highlightthickness = 0,
                                              font = font.Font(family = "Segoe UI", size = 14),
                                              yscrollcommand = self.trackedcourse_vertical_scrollbar.set,
                                              xscrollcommand = self.trackedcourse_horizontal_scrollbar.set,
                                              listvariable = self.display_tracked_course);
        self.trackedcourse_vertical_scrollbar.grid(row = 1, column = 1, sticky = self.ALL_STICK);
        self.trackedcourse_horizontal_scrollbar.grid(row = 2, column = 0, sticky = self.ALL_STICK);
        self.trackedcourse_panel.grid(row = 1, column = 0, sticky = self.ALL_STICK);
        self.trackedcourse_vertical_scrollbar.config(command = self.trackedcourse_panel.yview);
        self.trackedcourse_horizontal_scrollbar.config(command = self.trackedcourse_panel.xview);

        self.trackedcourse_control_frame = W.Frame(self.Fcurrentcourse, 90, 0, bg = '#B6B6B6');
        self.trackedcourse_control_frame.grid(row = 1, column = 2, sticky = self.ALL_STICK);
        self.reset_button_icon = W.OpenImage(CURR_WORKING_DIR / "pics" / "reset_button.png");
        self.reset_button = tk.Button(self.trackedcourse_control_frame, image = self.reset_button_icon,
                                      bd = 0, highlightthickness = 0, cursor = 'hand2');
        self.reset_button.bind('<Button-1>', self.reset_tracked_courses);
        self.reset_button.pack(anchor = tk.CENTER, pady = 10);
        self.delete_button_icon = W.OpenImage(CURR_WORKING_DIR / "pics" / "delete_button.png");
        self.delete_button = tk.Button(self.trackedcourse_control_frame, image=self.delete_button_icon,
                                      bd=0, highlightthickness=0, cursor='hand2');
        self.delete_button.bind('<Button-1>', self.delete_selected_tracked_courses);
        self.delete_button.pack(anchor = tk.CENTER, pady = 10);


        self.starttrack_button_frame = W.Frame(self.Fcurrentcourse, 400, 60);
        self.starttrack_button_frame.grid(row = 3, column = 0, columnspan = 3, sticky = self.ALL_STICK);
        self.starttrack_button_icon = W.OpenImage(CURR_WORKING_DIR/"pics"/"start_tracking_button.png");
        self.starttrack_button = tk.Button(self.starttrack_button_frame, image = self.starttrack_button_icon,
                                           bd=0, highlightthickness=0, cursor = 'hand2');

        def temp_func(event):
            self.tracked_courses.add("hi");

        self.starttrack_button.bind('<Button-1>', func=temp_func);
        self.starttrack_button.pack(pady = 15);

        self.Fcurrentcourse.columnconfigure(0, weight = 1);
        self.Fcurrentcourse.columnconfigure(1, weight = 1);
        self.Fcurrentcourse.columnconfigure(2, weight=1);
        self.Fcurrentcourse.rowconfigure(0, weight = 1);
        self.Fcurrentcourse.rowconfigure(1, weight = 1);

    def Setup_Term_Frame(self):
        self.term_label = tk.Label(self.searchcourse_term_frame, text="Term:",
                                   font=font.Font(family="Segoe UI", size=-15),
                                   bg='#ffffff');

        #print(self.search_fields)

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
                                              bd=0, highlightthickness=0, cursor = 'hand2');
        self.search_submit_button.pack(pady = 15);

        def search_button_func(event):
            try:
                self.CD = self.scrape_course_data(self.term_curr.get(), self.dept_curr.get(), self.code_curr.get());
                self.refresh_display_panel_to_show_courses()
            except self.SearchFailure:
                self.refresh_display_panel_to_show_meme();
                popmsg.showerror("Fatal Error occurred during Search", "There are several reasons that might lead to this error:\n \
1. One of your search fields might contain invalid input (CourseCode has to be valid).\n \
2. We can NOT find ANY courses that fulfils your search filter/parameter \n \
3. Your Internet Connection might be down \n \
4. There is a bug in our codes/system");

        self.search_submit_button.bind('<Button-1>', func=search_button_func);



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





