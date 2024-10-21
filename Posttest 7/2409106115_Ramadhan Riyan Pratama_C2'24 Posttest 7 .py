users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "user123", "role": "pengguna"}
}

movies = {
    1: {"judul": "Avengers: Endgame", "sisa_tiket": 100, "harga_tiket": 50000},
    2: {"judul": "Joker", "sisa_tiket": 80, "harga_tiket": 45000},
    3: {"judul": "Spider-Man: No Way Home", "sisa_tiket": 50, "harga_tiket": 55000}
}

transactions = {}  


def tampilkan_menu():
    print("""
==========================================
|       Sistem Pembelian Tiket Bioskop   |
==========================================
|              1. Registrasi             |
|              2. Login                  |
|              3. Keluar                 |
==========================================
""")


def registrasi_user(username, password):
    if username in users:
        print("Username sudah terdaftar.")
    else:
        users[username] = {"password": password, "role": "pengguna"}
        print(f"Registrasi berhasil! Selamat datang, {username}.")


def tampilkan_film():
    print("\n==== Daftar Film ====")
    for id_film, movie in movies.items():
        print(f"ID: {id_film}, Judul: {movie['judul']}, Sisa Tiket: {movie['sisa_tiket']}, Harga Tiket: {movie['harga_tiket']}")


def sistem_admin():
    while True:
        print("""
==========================================
|               Sistem Admin             |
==========================================
|              1. Tambah Film            |
|              2. Lihat Film             |
|              3. Update Film            |
|              4. Hapus Film             |
|              5. Logout                 |
==========================================
""")
        admin_choice = input("Pilih opsi: ")

        if admin_choice == "1":
            tambah_film()

        elif admin_choice == "2":
            tampilkan_film()

        elif admin_choice == "3":
            update_film()

        elif admin_choice == "4":
            hapus_film()

        elif admin_choice == "5":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")


def update_film():
    id_film = int(input("Masukkan ID film yang ingin diupdate: "))
    movie = movies.get(id_film)
    if movie:
        judul_baru = input(f"Masukkan judul baru (saat ini: {movie['judul']}): ") or movie["judul"]
        sisa_tiket_baru = int(input(f"Masukkan sisa tiket baru (saat ini: {movie['sisa_tiket']}): ") or movie["sisa_tiket"])
        harga_tiket_baru = int(input(f"Masukkan harga tiket baru (saat ini: {movie['harga_tiket']}): ") or movie["harga_tiket"])

        movie.update({
            "judul": judul_baru,
            "sisa_tiket": sisa_tiket_baru,
            "harga_tiket": harga_tiket_baru
        })
        print(f"Film dengan ID {id_film} berhasil diupdate.")
    else:
        print("Film tidak ditemukan.")


def tambah_film():
    id_film = len(movies) + 1
    judul_film = input("Masukkan judul film: ")
    sisa_tiket = int(input("Masukkan jumlah tiket: "))
    harga_tiket = int(input("Masukkan harga tiket: "))
    
    movies[id_film] = {"judul": judul_film, "sisa_tiket": sisa_tiket, "harga_tiket": harga_tiket}
    print(f"Film '{judul_film}' berhasil ditambahkan.")

def hapus_film ():
    id_film = int(input("Masukkan ID film yang ingin dihapus: "))
    if movies.pop(id_film, None):
        print(f"Film dengan ID {id_film} berhasil dihapus.")
    else:
        print("Film tidak ditemukan.")


def login_user(username, password):
    if username in users and users[username]["password"] == password:
        role = users[username]["role"]
        if role == "admin":
            sistem_admin()
        elif role == "pengguna":
            sistem_pengguna(username)
    else:
        print("Username atau password salah.")


def sistem_pengguna(username):
    while True:
        print("""
==========================================
|              Sistem Pengguna           |
==========================================
|              1. Lihat Film             |
|              2. Beli Tiket             |
|              3. Lihat Riwayat          |
|              4. Logout                 |
==========================================
""")
        user_choice = input("Pilih opsi: ")

        if user_choice == "1":
            tampilkan_film()

        elif user_choice == "2":
            beli_tiket(username)

        elif user_choice == "3":
            tampilkan_riwayat(username)

        elif user_choice == "4":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")


def beli_tiket(username):
    id_film = int(input("Masukkan ID film yang ingin dibeli: "))
    jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))

    movie = movies.get(id_film)
    if movie:
        if movie["sisa_tiket"] >= jumlah_tiket:
            total_harga = jumlah_tiket * movie["harga_tiket"]
            movie["sisa_tiket"] -= jumlah_tiket
            
            if username not in transactions:
                transactions[username] = []
            transactions[username].append({
                "judul_film": movie["judul"],
                "jumlah_tiket": jumlah_tiket,
                "total_harga": total_harga
            })
            print(f"Pembelian {jumlah_tiket} tiket untuk film '{movie['judul']}' berhasil. Total harga: Rp{total_harga}")
        else:
            print("Tiket tidak cukup tersedia.")
    else:
        print("ID film tidak ditemukan.")


def tampilkan_riwayat(username):
    print("\n==== Riwayat Pembelian ====")
    user_transactions = transactions.get(username, [])
    if user_transactions:
        for i, transaction in enumerate(user_transactions, start=1):
            print(f"{i}. Film: {transaction['judul_film']}, Jumlah Tiket: {transaction['jumlah_tiket']}, Total Harga: Rp{transaction['total_harga']}")
    else:
        print("Belum ada transaksi yang dilakukan.")


while True:
    tampilkan_menu()
    pilih = input("Pilih opsi: ")

    if pilih == "1":
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
        registrasi_user(username, password)

    elif pilih == "2":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        login_user(username, password)

    elif pilih == "3":
        print("Anda keluar dari aplikasi. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid.")
