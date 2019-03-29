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

##### smtp_engine.py #####
# This is a python module that is able to use the SMTP protocol to send message to a specified email account

#=======================================
#==          IMPORTS MODULE           ==
#=======================================
import smtplib, ssl;
import getpass;

#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
DEFAULT_SERVER_DOMAIN = "smtp.gmail.com";
SSL_PORT = 465;
TLS_PORT = 587;

#=======================================
#==            Source Code            ==
#=======================================

class SETUP_SMTP_CONNECTION_ERROR(Exception):
    pass;

class FAILED_TO_SENDMAIL(Exception):
    pass;

class LOGIN_FAILURE(Exception):
    pass;

class Email_Engine:
    default_server_domain = DEFAULT_SERVER_DOMAIN;
    ssl_port = SSL_PORT;
    tls_port = TLS_PORT;

    def __init__(self):
        self.ssl_context = ssl.create_default_context(); # This may not be needed!!!
        self.connection = None;

    def __del__(self):
        try:
            if self.connection != None:
                self.connection.quit();
                self.connection = None;
            
        except Exception:
            print('WARNINGS: Failure Detected during SMTP connection Closure!!');
            print('SMTP Connection Object is DELETED!!');
            print('Please RE-SETUP your SMTP Connection!!');

    @staticmethod
    def console_login():
        return (input("Please Enter Your Email Accout: "),input("Please Enter Your Password: "));

    def login(self, account_info: tuple):
        if self.connection != None:
            try:
                self.connection.login(account_info[0], account_info[1]);
            except:
                print()
                print("-------------------------- IMPORTANT!!!! --------------------------");
                print("If you are atttempting to send mails to a gmail-likewise account, ")
                print("     YOU MUST TURN ON THE FOLLOWING PERMISSION INSIDE YOUR EMAIL ACCOUNT:")
                print("              <Let less secure apps access your account>           ")
                print("-------------------------------------------------------------------")

                print("------------------------ FAILED TO LOGIN --------------------------")
                print("       !!!! PLEASE RECHECK YOUR ACCOUNT NAME AND PASSWORD !!!!     ")
                print("-------------------------------------------------------------------")

                self.__del__();

                raise LOGIN_FAILURE();

        else:
            raise LOGIN_FAILURE("Connection is not established");

    def sendmail(self, sender_email:str, recv_email:str, msg:str):
        if self.connection != None:
            try:
                self.connection.sendmail(sender_email, recv_email, msg);
            except:
                print()
                print("-------------------------- IMPORTANT!!!! --------------------------");
                print("If you are atttempting to send mails to a gmail-likewise account, ")
                print("     YOU MUST TURN ON THE FOLLOWING PERMISSION INSIDE YOUR EMAIL ACCOUNT:")
                print("              <Let less secure apps access your account>           ")
                print("-------------------------------------------------------------------")
                print()

                self.__del__();

                raise FAILED_TO_SENDMAIL();

        else:
            raise FAILED_TO_SENDMAIL("Connection is not established");

    def setup_tls_connection(self, server_domain = default_server_domain, port = tls_port):
        if self.connection == None:
            try:
                self.connection = smtplib.SMTP(server_domain, port);
                self.connection.ehlo();
                self.connection.starttls();
            except:
                raise SETUP_SMTP_CONNECTION_ERROR("Failed to establish TLS connection: Connection to server failed")
        else:
            raise SETUP_SMTP_CONNECTION_ERROR("Failed to establish TLS connection: Detected already established connection");

    def setup_ssl_connection(self, server_domain = default_server_domain, port = ssl_port):
        if self.connection == None:
            try:
                self.connection = smtplib.SMTP_SSL(server_domain, port, context= self.ssl_context);
            except:
                raise SETUP_SMTP_CONNECTION_ERROR("Failed to establish TLS connection: Connection to server failed")
        else:
            raise SETUP_SMTP_CONNECTION_ERROR("Failed to establish TLS connection: Detected already established connection ");


#=======================================
#==       DEBUGGING AND TESTING       ==
#=======================================

if __name__ == "__main__":
    EE = Email_Engine();
    EE.setup_tls_connection();
    EE.login(Email_Engine.console_login());
    EE.sendmail("tezktenr@gmail.com", "tezktenr@gmail.com", "Hi, This is an Educational Practice to use SMTP protocol to send emails");
    EE.__del__();
