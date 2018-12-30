##### HomePage.py #####
# This is a python module that creates the Homepage for UCI-Schedule-Assistant

#=======================================
#==            IMPORTS LIB            ==
#=======================================
import tkinter as tk
from tkinter import font
from tkinter import ttk
from PIL import ImageTk, Image

#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
debugging = True;
window_size = (1280,720);

#=======================================
#==            Source Code            ==
#=======================================

class Homepage:
    w,h = window_size;
    _menu_function_tags = ['Search Courses', 'View My Schedule'];

    def __init__(self):
        self.root = tk.Tk();
        self._setup_control();
        self._configure_root_window();
        self._configure_ttk_style();
        self._configure_ttk_map();
        self._retrieve_images();
        self._create_top_bar();
        self._create_welcome_banner();
        self._create_welcome_image();
        self._grid_layout();
        self.root.mainloop();

    def _setup_control(self):
        self.user_email = tk.StringVar();
        self.user_email.set("PeterAnteater@uci.edu")
        self._submit_button_txt = tk.StringVar();
        self._submit_button_txt.set("Submit Email")
        self._submit_button_status = False;

    def _retrieve_images(self):
        img = Image.open("quantum_wallpaper.jpg");
        img = img.resize((self.w, int(0.78125*self.h)), Image.ANTIALIAS)
        self._wallpaper = ImageTk.PhotoImage(img);
        img = Image.open("hamburger_menu.png");
        img = img.resize((int(0.03515625*self.w), int(0.04375*self.h)), Image.ANTIALIAS)
        self._hamburger_menu = ImageTk.PhotoImage(img);
        img = Image.open("Cancel_64px.png");
        img = img.resize((int(0.01953125*self.w),int(0.03125*self.h)), Image.ANTIALIAS)
        self._close_menu_cross = ImageTk.PhotoImage(img);

    def _configure_root_window(self):
        self.root.geometry(f"{self.w}x{self.h}+50+0");
        self.root.maxsize(self.w,self.h);
        self.root.minsize(self.w,self.h);
        self.root.title("UCI Schedule Assistant")

    def _configure_ttk_style(self):
        self.style = ttk.Style();
        self.style.theme_use("clam")
        self.style.configure("TopBar.TFrame", background = "#504D4D");
        self.style.configure("Welcome.TFrame", background = "#A4CEEF");
        self.style.configure("Welcome.TLabel", background = "#A4CEEF", anchor = tk.CENTER, justify = tk.CENTER, font = ("Comic Sans MS", int(0.05 * self.h)))
        self.style.configure("Menu.TButton", background = "#504D4D", borderwidth = 0);
        self.style.configure("Menu_inside.TButton", background = "#E0FBFF", borderwidth = 0, font = ("Segoe UI", int(0.025 * self.h), "bold italic"));
        self.style.configure("about.TButton", background="#504D4D", foreground = "#0090FF", width = 8, borderwidth=0, font = ("Segoe UI", int(0.02 * self.h), "bold italic"));
        self.style.configure("email.TEntry", fieldbackground="FFFFFF", foreground = "#000000");
        self.style.configure("submit.TButton", background="#5EF9F4", foreground = "#707070", width= 15, borderwidth=0, font = ("Segoe UI", int(0.02 * self.h), "bold"));
        self.style.configure("change.TButton", background ="#FE2323", foreground = "#000000", width = 15, borderwidth = 0, font = ("Segoe UI", int(0.02 * self.h), "bold"));
        self.style.configure("Menu.TFrame", background = "#E0FBFF");


    def _configure_ttk_map(self):
        self.style.map("Menu.TButton",
                       background = [('active', '#504D4D'), ('focus', '#504D4D'), ('pressed', '#504D4D')]
                       );
        self.style.map("about.TButton",
                       background = [('active', '#504D4D'), ('focus', '#504D4D'), ('pressed', '#504D4D')]
                       );
        self.style.map("email.TEntry",
                       fieldbackground = [('active', '#FFFFFF'), ('disabled', '#FF8000'),('readonly','#FF8000'), ('!focus', '#CBCBCB'), ('focus', '#FFFFFF')],
                       foreground = [('active', '#000000'), ('disabled', '#000000'), ('readonly', '#000000'), ('!focus', '#000000'), ('focus', '#000000')] );
        self.style.map("submit.TButton",
                       background = [('active', '#5EF9F4'), ('focus','#5EF9F4'), ('pressed', '#5EF9F4')]);
        self.style.map("change.TButton",
                       background=[('active', '#FE2323'), ('focus', '#FE2323'), ('pressed', '#FE2323')]);

    @staticmethod
    def wd(tkinter_obj):
        return tkinter_obj.winfo_reqwidth();

    def _create_menu_bar(self):

        def _create_function_buttons(self):
            for text in self._menu_function_tags:
                variable_name = '_' + text.replace(' ', '_') + '_button';
                exec(f"self.{variable_name} = ttk.Button(self._menu_bar, text = '{text}', cursor = 'hand2', width = 17, style = 'Menu_inside.TButton')");

        self._close_menu_bar();
        self._menu_bar = ttk.Frame(self.root, width=0.2734375 * self.w, height=self.h, style="Menu.TFrame");
        self._empty_r0_1 = ttk.Frame(self._menu_bar, width = 0.24609375 * self.w, height = 0.03125 * self.h, style = "Menu.TFrame");
        self._cancel_menu_button = ttk.Button(self._menu_bar, image=self._close_menu_cross, cursor="hand2", style="Menu_inside.TButton", \
                                              command=self._close_menu_bar);
        self._empty_r0_2 = ttk.Frame(self._menu_bar, width = 0.0078125 * self.w, height = 0.03125 * self.h, style = "Menu.TFrame")
        self._empty_r1_1 = ttk.Frame(self._menu_bar, width = 0.2734375 * self.w, height = 0.01 * self.h, style = "Menu.TFrame");
        self._empty_r2_1 = ttk.Frame(self._menu_bar, width = 0.0234375 * self.w, height=0.03125 * self.h, style="Menu.TFrame");
        _create_function_buttons(self);
        self._empty_r2_2 = ttk.Frame(self._menu_bar, width= self.wd(self._empty_r0_1) - self.wd(self._empty_r2_1) - self.wd(self._Search_Courses_button), height=0.03125 * self.h, style="Menu.TFrame");
        self._empty_r2_3 = ttk.Frame(self._menu_bar, width= self.wd(self._menu_bar) - self.wd(self._empty_r0_1), height=0.03125 * self.h, style="Menu.TFrame");
        self._bottom_empty = ttk.Frame(self._menu_bar, width = 0.2734375 * self.w, height = self.h, style="Menu.TFrame");
        self._open_menu_bar();

    def _open_menu_bar(self):

        def _grid_function_buttons(self):
            curr_row = 2;
            for text in self._menu_function_tags:
                variable_name = '_' + text.replace(' ', '_') + '_button';
                self._empty_r2_1.grid(row=curr_row, column=0, columnspan=1)
                self._Search_Courses_button.grid(row=2, column=1, columnspan=1)
                exec(f"self.{variable_name}.grid(row={curr_row}, column = 1, columnspan = 1)")
                self._empty_r2_2.grid(row=curr_row, column=2, columnspan=1)
                self._empty_r2_3.grid(row=curr_row, column=3, columnspan=2)
                curr_row += 1;
            return curr_row;



        self._menu_bar.place(x = 0, y = 0);
        self._empty_r0_1.grid(row = 0, column = 0, columnspan = 3)
        self._cancel_menu_button.grid(row = 0, column = 3, columnspan = 1)
        self._empty_r0_2.grid(row = 0, column = 4, columnspan = 1)
        self._empty_r1_1.grid(row = 1, column = 0, columnspan = 5)
        last_row = _grid_function_buttons(self);
        self._bottom_empty.grid(row = last_row, column = 0, columnspan = 5)


    def _close_menu_bar(self):
        try:
            self._menu_bar.destroy();
        except:
            pass;


    def _create_top_bar(self):

        def submit_change_email():
            self._close_menu_bar();
            self._submit_button_status = not self._submit_button_status;
            self._top_bar.destroy();
            self._create_top_bar();
            if self._submit_button_status:
                self._email_entry.configure(state = tk.DISABLED);
                self._submit_button_txt.set("Change Email")
            else:
                self._email_entry.configure(state = tk.NORMAL);
                self._submit_button_txt.set("Submit Email")
            self._grid_top_bar()

        self._top_bar = ttk.Frame(self.root, width = self.w, height = 0.0875 * self.h, style = "TopBar.TFrame");
        self._empty_top0 = ttk.Frame(self._top_bar, width=0.01171875 * self.w, height=0.0875 * self.h, style="TopBar.TFrame");
        self._menu_button = ttk.Button(self._top_bar, image = self._hamburger_menu, cursor = "hand2", style = "Menu.TButton", \
                                       command = self._create_menu_bar);
        self._empty_top1 = ttk.Frame(self._top_bar, width = 0.4414 * self.w, height = 0.0875 * self.h, style = "TopBar.TFrame");
        self._about_button = ttk.Button(self._top_bar, text = "About us", cursor = "hand2", style = "about.TButton")
        self._empty_top2 = ttk.Frame(self._top_bar, width= 0.02421875 * self.w, height=0.0875 * self.h, style="TopBar.TFrame");
        self._email_entry = ttk.Entry(self._top_bar, width = 25, textvariable = self.user_email, justify = tk.CENTER, \
                                      font= font.Font(family="Segoe UI", size=int(0.02 * self.h), weight="bold"),\
                                      style = "email.TEntry");
        self._empty_top3 = ttk.Frame(self._top_bar, width=0.01953125 * self.w, height=0.0875 * self.h, style="TopBar.TFrame");
        self._submit_button = ttk.Button(self._top_bar, textvariable = self._submit_button_txt, cursor = "hand2", \
                                         style = "change.TButton" if self._submit_button_status else "submit.TButton", \
                                         command = submit_change_email);
        self._empty_top4 = ttk.Frame(self._top_bar, \
                                     width= (self.w - self.wd(self._empty_top0)- self.wd(self._menu_button)- self.wd(self._empty_top1)- self.wd(self._about_button)- self.wd(self._empty_top2)- self.wd(self._email_entry)- self.wd(self._empty_top3)- self.wd(self._submit_button)), \
                                     height=0.0875 * self.h, style="TopBar.TFrame");

    def _create_welcome_banner(self):
        self._welcome_banner = ttk.Frame(self.root, width = self.w, height = 0.13125 * self.h, style = "Welcome.TFrame");
        self._welcome_label = ttk.Label(self.root, text = "Welcome to the UCI Schedule Assistant", style = "Welcome.TLabel")

    def _create_welcome_image(self):
        self._welcome_image = ttk.Label(self.root, image = self._wallpaper);

    def _grid_top_bar(self):
        self._top_bar.grid(row=0, column=0);
        self._empty_top0.grid(row=0, column=0)
        self._menu_button.grid(row=0, column=1);
        self._empty_top1.grid(row=0, column=2);
        self._about_button.grid(row=0, column=3);
        self._empty_top2.grid(row=0, column=4);
        self._email_entry.grid(row=0, column=5);
        self._empty_top3.grid(row=0, column=6);
        self._submit_button.grid(row=0, column=7);
        self._empty_top4.grid(row=0, column=8);

    def _grid_layout(self):
        self._grid_top_bar();
        self._welcome_banner.grid(row = 1, column = 0);
        self._welcome_label.grid(row = 1, column = 0);
        self._welcome_image.grid(row = 2, column = 0);






#=======================================
#==       DEBUGGING AND TESTING       ==
#=======================================
if __name__ == '__main__' and debugging:
    GUI = Homepage();