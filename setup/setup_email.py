import os
import getpass
import smtplib


class ConnectEmail:
    '''Handles everything related to database connection'''

    # check whether the file containing smtp data already exits
    @staticmethod
    def check_server_txt():
        return os.path.isfile('setup/smtp_data.txt')

    # gets data for SMTP server
    @staticmethod
    def prompt_smtp():
        fromaddr = 'dog5.laboratories@gmail.com'
        password = 'instancia'
        email_server = 'smtp.gmail.com, 587'

        sender = input("Email address of sender is dog5.laboratories@gmail.com by default. Do you want to change it? (Y/n) ")

        if sender.lower() == 'n':
            pass
        elif sender.lower() == 'y':
            fromaddr = input('Email address of sender: ')
            password = getpass.getpass()
            email_smtp = input('SMTP server is set to smtp.gmail.com/port: 587 by default. Do you want to change it? Y/n? ')
            if email_smtp.lower() == 'n':
                pass
            elif email_smtp.lower() == 'y':
                server = input("Your email providers smtp server: ")
                port = input('Port: ')
                email_server = '{}, {}'.format(server, port)
            else:
                fromaddr = 'dog5.laboratories@gmail.com'
                password = 'instancia'
                print("Not a valid option. We are going to use the default settings.")
        else:
            print("Not a valid option. We are going to use the default settings.")

        smtp_list = [fromaddr, password, email_server]

        with open('setup/smtp_data.txt', 'w') as myfile:
            for elem in smtp_list:
                myfile.writelines(elem  + '\n')
            print("SMTP settings have been saved.")

    # returns server connection object
    @classmethod
    def connect_server(cls):
        with open('setup/smtp_data.txt', 'r') as myfile:
            lines = myfile.readlines()
            smtp_from_file = [line.strip("\n") for line in lines]
            cls.fromaddr = smtp_from_file[0]
            cls.password = smtp_from_file[1]
            server = smtp_from_file[2].split(', ')
            server = tuple([server[0], int(server[1])])
            cls.server = smtplib.SMTP(server[0], server[1])
        return cls.server, cls.fromaddr, cls.password

    # this is what you need to call from main
    @classmethod
    def set_smtp(cls):
        if cls.check_server_txt():
            return cls.connect_server()
        else:
            cls.prompt_smtp()
            return cls.connect_server()
