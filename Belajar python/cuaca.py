def main():
    cuaca = input("Kondisi cuaca (panas/hujan/bagus): ")
    if cuaca == "panas":
        print('Gunakan payung')
    elif cuaca == "hujan":
        print('Gunakan payung')
    elif cuaca == "bagus":
        print('Tidak perlu mengunakan payung')
    else:
        print('Silahkan pilih sesuai opsi yang ada')
        main()
    
if __name__=='__main__':
    main()