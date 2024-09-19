from libs import welcome_message, exit_program
from games import bear
from tools import quiz

def menu():
    while True:
        print('\nMenu program:\n1.bear games\n2.quiz games\n3.keluar program')
        menu_user = int(input('Pilih menu: '))
        if menu_user == 1:
            bear.start()
        elif menu_user == 2:
            quiz.game()
        elif menu_user == 3:
            exit_program()
        else:
            print('Hanya boleh pilih yang di menu!!!')
        
def main():
    welcome_message()
    menu()

if __name__ == '__main__':
    main()



