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

##### Pages.py #####
# This is a python module that declares the base class <Pages>

#=======================================
#==            IMPORTS LIB            ==
#=======================================
import tkinter as tk
import GuiWidgets as W;

from os import sys, path
sys.path.append(path.dirname(path.dirname(__file__)))
import smtp_engine
import web_scrape_engine
import update_course_data
import course_data_decoder


#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
DEBUGGING = True;

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


class Pages:

    class PageHasInvalidSize(Exception):
        pass;

    class SendMailMustReceiveTextAsArguments(Exception):
        pass;

    class SearchFailure(Exception):
        pass;

    ALL_STICK = tk.N + tk.S + tk.W + tk.E;

    def __init__(self, MainFrame, account_name, account_password):
        self.MainFrame = MainFrame;
        w,h = self.page_size();
        self.PageFrame = W.Frame(self.MainFrame, w, h);
        self.PageFrame.pack();

        self.account_name = account_name;
        self.account_password = account_password;

        self._switch_page = False;

    def send_email(self, acc_name, acc_pw, *args):

        email_engine = smtp_engine.Email_Engine();

        email_engine.setup_tls_connection();
        email_engine.login((acc_name,acc_pw));
        for msg in args:
            if type(msg) != str:
                raise self.SendMailMustReceiveTextAsArguments("SendMail Receive Non-Str Arguments: {} whose type is {}".format(msg, type(msg)));
            else:
                email_engine.sendmail(acc_name, acc_name, msg);
        email_engine.__del__();

    def scrape_course_data(self, term_curr = "", dept_curr = "", code_curr = ""):
        user_input_dict = {"YearTerm":self.search_fields["YearTerm"][term_curr],
                           "Dept":self.search_fields["Dept"][dept_curr],
                           "CourseCodes":code_curr};
        try:
            engine = web_scrape_engine.web_scrape_engine(user_input_dict);
            course_data = engine.extract_data();
            print(course_data)
            if course_data == None:
                raise self.SearchFailure("course_data = None");
            return course_data_decoder.CourseDecoder(course_data);
        except:
            raise self.SearchFailure("fatal error during search");


    def switch(self):
        return self._switch_page;

    def page_size(self) -> tuple:
        return ( self.MainFrame.cget("width") , self.MainFrame.cget("height") );

    def get_account_info(self):
        return (self.account_name, self.account_password);

    def update(self):
        self.PageFrame.update();

    def destroy(self):
        self.PageFrame.destroy();