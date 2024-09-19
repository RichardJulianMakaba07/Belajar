import socket
from time import sleep

pc_names = socket.gethostname()

def welcome_message():
    style = "*" * (len(pc_names) + 6)
    print(style)
    print(f"** {pc_names} **")
    print(style)
    
def exit_program():
    print('\nProgram akan dihentikan')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Program berhasil dihentikan\n')
    exit()
    
