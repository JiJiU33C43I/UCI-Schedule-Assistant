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

class SETUP_SMTP_CONNECTION_ERROR(Exception):
    pass;

class CONNECTION_HAS_NOT_BEEN_ESTABLISHED(Exception):
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
            print('Failed to Close SMTP connection!!');
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

        else:
            raise CONNECTION_HAS_NOT_BEEN_ESTABLISHED();

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

        else:
            raise CONNECTION_HAS_NOT_BEEN_ESTABLISHED();

    def setup_tls_connection(self, server_domain = default_server_domain, port = tls_port):
        if self.connection == None:
            self.connection = smtplib.SMTP(server_domain, port);
            self.connection.ehlo();
            self.connection.starttls();
        else:
            raise SETUP_SMTP_CONNECTION_ERROR("Failed to establish TLS connection: Detected already established connection ");

    def setup_ssl_connection(self, server_domain = default_server_domain, port = ssl_port):
        if self.connection == None:
            self.connection = smtplib.SMTP_SSL(server_domain, port, context= self.ssl_context);
        else:
            raise SETUP_SMTP_CONNECTION_ERROR("Failed to establish TLS connection: Detected already established connection ");


if __name__ == "__main__":
    EE = Email_Engine();
    EE.setup_tls_connection();
    EE.login(Email_Engine.console_login());
    EE.sendmail("tezktenr@gmail.com", "tezktenr@gmail.com", "Hi, This is an Educational Practice to use SMTP protocol to send emails");
