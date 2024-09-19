import random
import main

def start():
    nama_user = input("\nMasukkan nama anda: ")
    while nama_user == "":
        nama_user = input("Harus diisi brow namanya: ")

    while True:
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4
        
        posisi_beruang = random.randint(1, 4)
        
        goa = goa_kosong.copy()
        goa[posisi_beruang - 1] = "|0_0|"
        goa_kosong = '  ' .join(goa_kosong)
        goa = '  ' .join(goa) 

        print(f"\nHalo {nama_user}!! coba perhatikan goa di bawah ini!!!")
        print(f"\n{goa_kosong}\n")
        print("Silahkan tebak di goa manakah yang terdapat beruang madu, apakah di goa 1/2/3/4 ?? ")

        pilihan_user = int(input("Masukkan jawaban anda: "))

        print("\nApakah anda sudah yakin dengan jawaban anda?")

        validasi_user = input("y/n: ")

        if validasi_user == "y":
            if pilihan_user == posisi_beruang:
                print(f"\n{goa}\n\nSELAMAT ANDA MENANG 🤩🏆🏆🏆\n")
            else:
                print(f"\n{goa}\n\nSAYANG SEKALI ANDA KALAH🤡🤣\n")
            
        elif validasi_user == "n":
            print("\n Silahkan masukkan jawaban anda sekali lagi!!!")
            jawaban_baru = int(input("Isi jawaban anda: "))
            if jawaban_baru == posisi_beruang:
                print(f"\n{goa}\n\nSELAMAT ANDA MENANG 🤩🏆🏆🏆\n")
            else:
                print(f"\n{goa}\n\nSAYANG SEKALI ANDA KALAH🤡🤣\n")
            
        else:
            print("Silahkan ulangi lagi!!!")
            exit()
            
        play_again = input("Apakah anda masih ingin melanjutkan permainan? [y/n]: ")
        if play_again == "n":
            main.menu()
        
if __name__ == '__main__':
    start()