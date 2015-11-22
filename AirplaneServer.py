import threading
import socket
import time
import os

__author__ = 'Francisc'

class AirplaneTypes:

    def __init__(self):
        pass

    def boeing(self):
        pass

    def airbus(self):
        pass

    def new_airplane_brand(self):
        pass

def server_user():
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    username = raw_input("                                    "
                         "             Representative's Name: ")
    user_password = raw_input("                                    "
                              "             Representative's Password: ")


def main():
    os.system('cls')
    server_user()
    #print "<<<<Welcome to the Airplane Reservation Server>>>>\n"
    #print "Representative Name: "

if __name__ == '__main__':
    main()

