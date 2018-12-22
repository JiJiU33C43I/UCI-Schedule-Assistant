'''
User Interface of UCI Schedule Assistant
Yuzhao Liu
'''

#================
#== IMPORT LIB ==
#================
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

#==================
#== IMPORT FILES ==
#==================
from SignUp import SignUp



#======================
#== GLOBAL CONSTANTS ==
#======================



#=============
#== SCRIPTS ==
#=============

#--------------
#-- TK ClASS --
#--------------
class GUI():

    #----------------
    #-- Class Body --
    #----------------
    def __init__(self, width=500, height=500):

        #--------------------
        #-- Class Variable --
        #--------------------
        self.notification = True

        #------------------
        #-- Class Method --
        #------------------
        self.root = tk.Tk()
        self.root.title("UCI Class Enrollment System")
        self.restrict_window_size(width, height)
        self.create_menu()
        self.create_mainbuttons()


    def restrict_window_size(self, root_width, root_height):
         self.root.minsize(width = root_width, height = root_height)
         self.root.maxsize(width = root_width, height = root_height)

    def create_menu(self):
        self.menu = tk.Menu(self.root, tearoff = 0)
        self.root.config(menu = self.menu)
        #self.root["menu"] = self.menu ## alternative way for config

        # Add the sign up/log in drop down menu
        self.SignUp_LogIn_menu = tk.Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = "Sign Up/Log In", menu = self.SignUp_LogIn_menu)
        self.SignUp_LogIn_menu.add_command(label = "Sign Up", command = self._sign_up)
        self.SignUp_LogIn_menu.add_command(label = "Log In", command = doNothing)

        # Add the other menu functions
        self.menu.add_command(label = "Student information")
        self.menu.add_command(label = "Notification", command = self._notification)
        self.menu.add_command(label = "About us", command = self._show_AboutUs_info)
    
    def create_mainbuttons(self):
        self.s = ttk.Style()
        self.s.theme_use("default")

        self.s.map("Main_Buttons.TButton", background=[("!active","grey"),("active","yellow3")], foreground=[("!active","white"),("active","white")])

        self.SearchClassButton          = ttk.Button(self.root, text = "Search Class", command = doNothing, takefocus = False, style = "Main_Buttons.TButton")
        self.ViewMyScheduleButton       = ttk.Button(self.root, text = "View My Schedule", command = doNothing, takefocus = False, style = "Main_Buttons.TButton")
        self.ClassExtendedButton        = ttk.Button(self.root, text = "Class Extended", command = doNothing, takefocus = False, style = "Main_Buttons.TButton")
        self.CourseTreeButton           = ttk.Button(self.root, text = "Course Tree", command = doNothing, takefocus = False, style = "Main_Buttons.TButton")
        self.FutureScheduleButton       = ttk.Button(self.root, text = "Future Schedule", command = doNothing, takefocus = False, style = "Main_Buttons.TButton")
        self.AutoEnrollmentSystemButton = ttk.Button(self.root, text = "Auto-Enrollment System", command = doNothing, takefocus = False, style = "Main_Buttons.TButton")

        self.SearchClassButton.grid(            column = 0, row = 0, sticky="nesw")
        self.ViewMyScheduleButton.grid(         column = 0, row = 1, sticky="nesw")
        self.ClassExtendedButton.grid(          column = 0, row = 2, sticky="nesw")
        self.CourseTreeButton.grid(             column = 0, row = 3, sticky="nesw")
        self.FutureScheduleButton.grid(         column = 0, row = 4, sticky="nesw")
        self.AutoEnrollmentSystemButton.grid(   column = 0, row = 5, sticky="nesw")
    
    
    #-------------------------
    #-- Assistant Functions --
    #-------------------------

    def _sign_up(self):
        sign_up_root = tk.Toplevel(self.root)
        signup_program = SignUp(sign_up_root)
        signup_program.mainloop()
        
        

    def _notification(self):
        print("notification")
        self.answer = tkinter.messagebox.askquestion("Turn On/Off Notifications", "Click: \n    Yes to turn On; No to turn Off")
        if self.answer == "yes":
            if self.notification == True:
                tkinter.messagebox.showinfo("Error:", "Notification has already been turned on")
            elif self.notification == False:
                tkinter.messagebox.showinfo("Success!", "Notification has been turned On")
                self.notification = True
        elif self.answer == "no":
            if self.notification == False:
                tkinter.messagebox.showinfo("Error:", "Notification has already been turned off")
            elif self.notification == True:
                tkinter.messagebox.showinfo("Success!", "Notification has been turned Off")
                self.notification = False

    def _show_AboutUs_info(self):
        tkinter.messagebox.showinfo("About Us", "Author: Arthur Liu")

    #-----------------------------
    #-- Execute the Tkinter Loop--
    #-----------------------------
    def mainloop(self):
        self.root.mainloop()
    


#======================
#== TESTING FUNCTION ==
#======================
def doNothing():
    print("Yes")




#=================
#== RUN PROGRAM ==
#=================
if __name__ == "__main__":
    program = GUI(width = 1300, height = 800)
    program.mainloop()


