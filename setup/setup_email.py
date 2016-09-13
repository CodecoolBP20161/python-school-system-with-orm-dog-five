import os
import getpass
import smtplib
import json


class ConnectEmail:
    '''Handles everything related to e-mail connection'''

    __default = {'fromaddr': 'dog5.laboratories@gmail.com',
                 'password': 'instancia',
                 'smtp_addr': 'smtp.gmail.com',
                 'port': 587}

    def __init__(self, fromaddr, password, smtp_addr, port):
        self.fromaddr = fromaddr
        self.password = password
        self.server = smtplib.SMTP(smtp_addr, port)

    @classmethod
    def build_from_file(cls):
        if os.path.isfile('setup/smtp_data.json'):
            with open('setup/smtp_data.json', 'r') as infile:
                data = json.load(infile)
        else:
            data = cls.get_user_data()
        return cls(**data)

    @classmethod
    def get_user_data(cls):
        choice = input('Use default? Press (y) for yes.\n')
        if choice == 'y':
            data = cls.__default
        else:
            fromaddr = input('Email address of sender: ')
            password = getpass.getpass()
            smtp_addr = input('SMTP server address:')
            port = int(input('Port: '))
            data = {'fromaddr': fromaddr,
                    'password': password,
                    'smtp_addr': smtp_addr,
                    'port': port}
        with open('setup/smtp_data.json', 'w') as outfile:
            json.dump(data, outfile)
        return data
