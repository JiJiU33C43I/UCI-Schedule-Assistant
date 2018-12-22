'''
SignUp Class of GUI
Yuzhao Liu 
'''

#================
#== IMPORT LIB ==
#================
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

#===================
#== SIGN_UP CLASS ==
#===================
class SignUp():
    def __init__(self, root, width = 300, height = 120):
        print("signup")
        self.root = root
        self.root.title("New User Sign Up")
        self.restrict_window_size(width, height)
        self.create_info_entries()
        self.create_submit_button()
        

    def restrict_window_size(self, root_width, root_height):
         self.root.minsize(width = root_width, height = root_height)
         self.root.maxsize(width = root_width, height = root_height)
    
    def create_info_entries(self):
        self.username_label = tk.Label(self.root, text="User Name: ") 
        self.username_entry = tk.Entry(self.root)
        self.password_label = tk.Label(self.root, text="Password: ")
        self.password_entry = tk.Entry(self.root)
        self.retype_password_label = tk.Label(self.root, text="Retype your Password: ")
        self.retype_password_entry = tk.Entry(self.root)
        self.email_label = tk.Label(self.root, text="Email: ")
        self.email_entry = tk.Entry(self.root)

        self.username_label.grid(column = 0, row = 0, sticky = "e")
        self.username_entry.grid(column = 1, row = 0, sticky = "nesw")
        self.password_label.grid(column = 0, row = 1, sticky = "e")
        self.password_entry.grid(column = 1, row = 1, sticky = "nesw")
        self.retype_password_label.grid(column = 0, row = 2, sticky = "e")
        self.retype_password_entry.grid(column = 1, row = 2, sticky = "nesw")
        self.email_label.grid(column = 0, row = 3, sticky = "e")
        self.email_entry.grid(column = 1, row = 3, sticky = "nesw")

    def create_submit_button(self):
        self.s = ttk.Style()
        self.s.theme_use("default")

        self.s.map("Main_Buttons.TButton", background=[("!active","grey"),("active","yellow3")], foreground=[("!active","white"),("active","white")])
        
        # for now it will only quit the sign up window; need to implement store function
        self.SubmitButton = ttk.Button(self.root, text = "Submit", command = self.root.destroy, takefocus = False, style = "Main_Buttons.TButton")
        self.SubmitButton.grid(column = 1, row = 5)#, sticky = "esw")

    def mainloop(self):
        self.root.mainloop()

    #-------------------------
    #-- ASSISTANT FUNCTIONS --
    #-------------------------

    #def _submit_and_quit(self):  
    #    self.root.destroy()





