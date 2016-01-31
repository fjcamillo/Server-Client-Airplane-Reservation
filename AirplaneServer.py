import os
import socket
import time


class ServerApplications:

    def __init__(self):
        self.menu_holder = ''

    def manage_account(self):
        os.system('cls')
        print("Welcome to Account Manager")
        print("=================================")
        print()


    def view_flight_status(self):
        pass

    def create_flight(self):
        pass

    def confirm_flight(self):
        pass

    def restart_class(self):
        pass


def landing_page():
    print("<<<Welcome to the Airplane Server Side App>>>\n")
    print("Name: " + """
A. Manage Account
B. View Flight Status
C. Create a Flight for Booking
D. Confirm a Flight Booking Request
E. Exit
        """)
    task_to_do = input("\nChoose the task to do: ")
    live_account = ServerApplications()
    if task_to_do.lower() == 'a':
        live_account.manage_account()
    elif task_to_do.lower() == 'b':
        live_account.view_flight_status()
    elif task_to_do.lower() == 'c':
        live_account.create_flight()
    elif task_to_do.lower() == 'd':
        live_account.confirm_flight()
    elif task_to_do.lower() == 'e':
        exit()
    else:
        print("You typed something wrong. Please choose again!")
        input("<<<Press Enter>>>")
        os.system('cls')
        landing_page()

def start_server():
    print("Program will now connect to localhost")
    time.sleep(2)
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))
    #s.listen(1             # '#' line will only be added if needed
    #c, address = s.accept()


def loading_bar():
    os.system('cls')
    print("-Loading-")
    for i in range(0, 11, 1):
        if i == 0:
            print("[", end='')
            time.sleep(2)
        elif i == 10:
            print("]")
            time.sleep(2)
        else:
            print("#", end='')
            time.sleep(1)
def main():
    os.system('cls')
    loading_bar()
    start_server()
    landing_page()

if __name__ == '__main__':
    main()