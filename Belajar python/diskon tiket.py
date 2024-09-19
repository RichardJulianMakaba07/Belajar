jumlah_pembelian = int(input('Masukkan jumlah pembelian tiket: '))

if jumlah_pembelian >= 3:
    for i in range(jumlah_pembelian): 
        umur_pengunjung = int(input('Umur pengunjung: '))
        if umur_pengunjung == umur_pengunjung:
            print('Tidak boleh sama umurnya')
            if umur_pengunjung < 12:
                print('mendapat diskon 17%')
            elif 12 <= umur_pengunjung <= 18:
                print('mendapat diskon 13%')
            else:
                print('mendapat diskon 10%')
              
else:
    print('Tidak memenuhi syarat untuk mendapat diskon')