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

while True:
    print("""
==========================================
|       Sistem Pembelian Tiket Bioskop   |
==========================================
|              1. Registrasi             |
|              2. Login                  |
|              3. Keluar                 |
==========================================
""")
    pilih = input("Pilih opsi: ")

    if pilih == "1":
        username = input("Masukkan username baru: ")
        if username in users:
            print("Username sudah terdaftar.")
        else:
            password = input("Masukkan password baru: ")
            users[username] = {"password": password, "role": "pengguna"}
            print(f"Registrasi berhasil! Selamat datang, {username}.")

    elif pilih == "2":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            if role == "admin":
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
                        id_film = len(movies) + 1
                        judul_film = input("Masukkan judul film: ")
                        sisa_tiket = int(input("Masukkan jumlah tiket: "))
                        harga_tiket = int(input("Masukkan harga tiket: "))
                        movies[id_film] = {"judul": judul_film, "sisa_tiket": sisa_tiket, "harga_tiket": harga_tiket}
                        print(f"Film '{judul_film}' berhasil ditambahkan.")

                    elif admin_choice == "2":
                        print("\n==== Daftar Film ====")
                        for id_film, movie in movies.items():
                            print(f"ID: {id_film}, Judul: {movie['judul']}, Sisa Tiket: {movie['sisa_tiket']}, Harga Tiket: {movie['harga_tiket']}")

                    elif admin_choice == "3":
                        id_film = int(input("Masukkan ID film yang ingin diupdate: "))
                        movie = movies.get(id_film)
                        if movie:
                            movie.update({
                                "judul": input(f"Masukkan judul baru (saat ini: {movie['judul']}): ") or movie["judul"],
                                "sisa_tiket": int(input(f"Masukkan sisa tiket baru (saat ini: {movie['sisa_tiket']}): ") or movie["sisa_tiket"]),
                                "harga_tiket": int(input(f"Masukkan harga tiket baru (saat ini: {movie['harga_tiket']}): ") or movie["harga_tiket"])
                            })
                            print(f"Film dengan ID {id_film} berhasil diupdate.")
                        else:
                            print("Film tidak ditemukan.")

                    elif admin_choice == "4":
                        id_film = int(input("Masukkan ID film yang ingin dihapus: "))
                        if movies.pop(id_film, None):
                            print(f"Film dengan ID {id_film} berhasil dihapus.")
                        else:
                            print("Film tidak ditemukan.")

                    elif admin_choice == "5":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid.")

            elif role == "pengguna":
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
                        print("\n==== Daftar Film ====")
                        for id_film, movie in movies.items():
                            print(f"ID: {id_film}, Judul: {movie['judul']}, Sisa Tiket: {movie['sisa_tiket']}, Harga Tiket: {movie['harga_tiket']}")

                    elif user_choice == "2":
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

                    elif user_choice == "3":
                        print("\n==== Riwayat Pembelian ====")
                        user_transactions = transactions.get(username, [])
                        if user_transactions:
                            for i, transaction in enumerate(user_transactions, start=1):
                                print(f"{i}. Film: {transaction['judul_film']}, Jumlah Tiket: {transaction['jumlah_tiket']}, Total Harga: Rp{transaction['total_harga']}")
                        else:
                            print("Belum ada transaksi yang dilakukan.")

                    elif user_choice == "4":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid.")
        else:
            print("Username atau password salah.")

    elif pilih == "3":
        print("Anda keluar dari aplikasi. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid.")
