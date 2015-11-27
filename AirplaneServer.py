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

# --------------------Account Class--------------------


class Accounts:

    def __init__(self):
        self.account_database = {}

    def old_account(self, account_username, account_password):

        if str(account_username) in self.account_database:

            for_checking = self.account_database[str(account_username)]
            if str(account_password) == str(for_checking):
                print "Account Verified."
                input()
        else:
            print "Account is not in our Database"
            countdown()
            server_user()

    def new_account(self, new_account_username, new_account_password):
        self.account_database[str(new_account_username)] = str(new_account_password)
        print "Account Added to Database"


class Pages():
    def __init__(self):
        pass

    def first_page(self):
        print "Welcome to the Flight Reservation Module"
        print "Representative's Name: ", str(Accounts)


def countdown():
    for i in range(5, 0, 1):
        print str(i)
        time.sleep(1)


def server_user():
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

    print "                                                           " \
          "<<< Welcome to the Airplane Reservation Server >>>"
    status = raw_input("                                                           "
                       "Do you have an account? [Y/N]: ")

    if status.lower() == 'y':
        os.system('cls')
        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        username = raw_input("                                    "
                             "             Representative's Name: ")
        user_password = raw_input("                                    "
                                  "             Representative's Password: ")
        open_account = Accounts()
        open_account.old_account(username, user_password)

    elif status.lower() == 'n':
        os.system('cls')
        new_account_name = raw_input("Name: ")
        new_account_pass = raw_input("Password: ")

        open_account = Accounts()
        open_account.new_account(str(new_account_name), str(new_account_pass))

    else:
        pass




def main():
    os.system('cls')
    server_user()

if __name__ == '__main__':
    main()


