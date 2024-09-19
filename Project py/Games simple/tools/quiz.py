import main
import random
from time import sleep

def start_program():
    print('\nQuiz akan dimulai dalam')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...Have Fun')
    sleep(1)
    print('Quiz dmulai\n')
    
def next_program():
    print('\nSoal selanjutnya')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...Have Fun')
    
def game():
    print('\nHALLOOOOOOO')
    user_name = input('Your name: ')
    user_name = user_name.upper()
    while user_name == '':
        user_name = input('Your name: ')
        user_name = user_name.upper()
    print(f'WELCOME TO QUIZ {user_name}')
    start_program()
        
    while True:
        soal = ['Apa sungai terpanjang di dunia?', 'Siapa yang melukis Mona Lisa?', 'Apa nama perusahaan teknologi terbesar di Korea Selatan?', 'Apa organ terbesar dalam tubuh manusia?', 'Berapa hari dalam setahun pada tahun kabisat?', 'Apa ibu kota Portugal?']
        urutan_soal = random.choice(soal)
        answer = input(urutan_soal)
        answer = answer.lower()
        
        if urutan_soal == soal[0]:
            if answer == 'sungai nil' or 'nil' :
                print('BENARRR')
            else:
                print('SALAHHH')
            
        if urutan_soal == soal[1]: 
            if answer == 'leonardo da vinci':
                print('BENARRR')
            else:
                print('SALAHHH')
            
        if urutan_soal == soal[2]:
            if answer == 'samsung':
                print('BENARRR')
            else:
                print('SALAHHH')
            
        if urutan_soal == soal[3]:
            if answer == 'kulit':
                print('BENARRR')
            else:
                print('SALAHHH')
            
        if urutan_soal == soal[4]:
            if answer == '366':
                print('BENARRR')
            else:
                print('SALAHHH')
            
        if urutan_soal == soal[5]:
            if answer == 'lisbon':
                print('BENARRR')
            else:
                print('SALAHHH')
        
        play_again = input("Apakah anda masih ingin melanjutkan permainan? [y/n]: ")
        if play_again == "n":
            main.menu()
        next_program()
          
            
if __name__ == '__main__':
    game()           