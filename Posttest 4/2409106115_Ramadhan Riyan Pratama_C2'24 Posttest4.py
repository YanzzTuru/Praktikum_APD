def login():
    username_terdaftar = "ramadhan"
    password_terdaftar = "115"
    kesempatan = 3

    while kesempatan > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username == username_terdaftar and password_terdaftar == password_terdaftar:
            print("Login berhasil!")
            return True
        else:
            kesempatan -= 1
            print(f"Username atau password salah! Kesempatan tersisa: {kesempatan}\n")
            
    print("Anda salah memasukan username dan password. Program berhenti.")
    return False


def program_utama():
    while True:
        print("Daftar Mobil dan Diskon")
        print("1. Tesla (Diskon 17%)")
        print("2. Toyota (Diskon 21%)")
        print("3. Hyundai (Diskon 23%)")
        print("4. Keluar")

        pilihan = input("\Masukkan pilihan Anda (1/2/3/4): ")

        if pilihan == "1":
            harga_awal = float(input("Masukkan harga mobil Tesla: Rp "))
            diskon = 0.17 * harga_awal
            harga_akhir = harga_awal - diskon
            print(f"Harga setelah diskon Tesla: Rp {harga_akhir}\n")
        
        elif pilihan == "2":
            harga_awal = float(input("Masukkan harga mobil Toyota: Rp "))
            diskon = 0.21 * harga_awal
            harga_akhir = harga_awal - diskon
            print(f"Harga setelah diskon Toyota: Rp {harga_akhir}\n")
        
        elif pilihan == "3":
            harga_awal = float(input("Masukkan harga mobil Hyundai: Rp "))
            diskon = 0.23 * harga_awal
            harga_akhir = harga_awal - diskon
            print(f"Harga setelah diskon Hyundai: Rp {harga_akhir}\n")
        
        elif pilihan == "4":
            print("anda tidak memilih mobil apapun.Program berhenti.")
            break
        
        else:
            print("Pilihan tidak valid! Coba lagi.")

if login():
    program_utama()
