import json

# Data motor disimpan dalam file JSON
data_motor_file = 'data_motor.json'

# Fungsi untuk membaca data motor dari file JSON
def read_motor_data():
    try:
        with open(data_motor_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Fungsi untuk menulis data motor ke file JSON
def write_motor_data(data):
    with open(data_motor_file, 'w') as file:
        json.dump(data, file)

# Fungsi untuk menampilkan menu admin
def admin_menu():
    while True:
        print("\nMenu Admin")
        print("1. Tambah Motor")
        print("2. Lihat Motor")
        print("3. Update Motor")
        print("4. Hapus Motor")
        print("5. Keluar")
        
        choice = input("Pilih menu: ")
        if choice == '1':
            add_motor()
        elif choice == '2':
            view_motor()
        elif choice == '3':
            update_motor()
        elif choice == '4':
            delete_motor()
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi untuk menambah motor
def add_motor():
    motor = input("Masukkan nama motor: ")
    data_motor = read_motor_data()
    data_motor.append(motor)
    write_motor_data(data_motor)
    print("Motor berhasil ditambahkan.")

# Fungsi untuk melihat motor
def view_motor():
    data_motor = read_motor_data()
    print("Daftar Motor:")
    for motor in data_motor:
        print(motor)

# Fungsi untuk update motor
def update_motor():
    view_motor()
    index = int(input("Pilih indeks motor untuk diupdate: ")) - 1
    new_name = input("Masukkan nama motor baru: ")
    data_motor = read_motor_data()
    data_motor[index] = new_name
    write_motor_data(data_motor)
    print("Motor berhasil diupdate.")

# Fungsi untuk hapus motor
def delete_motor():
    view_motor()
    index = int(input("Pilih indeks motor untuk dihapus: ")) - 1
    data_motor = read_motor_data()
    data_motor.pop(index)
    write_motor_data(data_motor)
    print("Motor berhasil dihapus.")

# Fungsi untuk registrasi pengguna
def register_user():
    # Implementasi registrasi pengguna
    pass

# Fungsi utama untuk login
def main():
    user_type = input("Masukkan jenis pengguna (Admin/User): ")
    if user_type.lower() == 'admin':
        admin_menu()
    elif user_type.lower() == 'user':
        register_user()
    else:
        print("Jenis pengguna tidak valid.")

if __name__ == "__main__":
    main()
