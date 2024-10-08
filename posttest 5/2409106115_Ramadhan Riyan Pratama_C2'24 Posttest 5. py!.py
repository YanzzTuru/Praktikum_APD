users = [["admin", "admin123", "admin"]]

movies = [[1, "Film Transformer One", 50, 55000], [2, "Film Fast And Furious", 30, 45000], [3, "Film One Piece Red", 20, 60000]]

transactions = []



while True:
    try:
        print("""
==========================================
|          Sistem Login Aplikasi:        |
==========================================
|              1. Registrasi             |
|              2. Login                  |
|              3. Exit                   |
==========================================

""")
        pilih = int(input("Pilih opsi: "))

        if pilih == 1:
            print("==== Registerasi ====")
            username = input("Masukkan username baru: ")
            password = input("Masukkan password baru: ")
            role = input("Masukkan peran (admin/pengguna): ").lower()

            if role not in ["admin", "pengguna"]:
                raise ValueError("Peran tidak valid. Pilih 'admin' atau 'pengguna'.")
            
            users.append([username, password, role])
            print(f"Registrasi berhasil untuk {username} sebagai {role}.")
        
        elif pilih == 2:
            print("\n==== Login ====")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            
            for user in users:
                if user[0] == username and user[1] == password:
                    logged_in_user = user
                    print(f"Login berhasil! Selamat datang, {logged_in_user[0]}.")
                    break
            else:
                raise ValueError("Username atau password salah.")

            if logged_in_user[2] == "admin":
                
                while True:
                    print("""
==========================================
|               Sistem Admin             |
==========================================
|              1. Tambah Film            |
|              2. Lihat Film             |
|              3. Update Film            |
|              4. Hapus Film             |
|              5. Log Out                |
==========================================

""")
                    admin_choice = int(input("Pilih opsi: "))

                    if admin_choice == 1:
                        print("\n==== Tambah Film ====")
                        id_film = len(movies) + 1
                        judul_film = input("Masukkan judul film: ")
                        sisa_tiket = int(input("Masukkan jumlah tiket: "))
                        harga_tiket = int(input("Masukkan harga tiket: "))
                        movies.append([id_film, judul_film, sisa_tiket, harga_tiket])
                        print(f"Film '{judul_film}' berhasil ditambahkan.")

                    elif admin_choice == 2:
                        print("\n==== Daftar Film ====")
                        for movie in movies:
                            print(f"ID: {movie[0]}, Judul: {movie[1]}, Sisa Tiket: {movie[2]}, Harga Tiket: {movie[3]}")

                    elif admin_choice == 3:
                        print("\n==== Update Film ====")
                        id_film = int(input("Masukkan ID film yang ingin diupdate: "))
                        for movie in movies:
                            if movie[0] == id_film:
                                movie[1] = input(f"Masukkan judul baru untuk film {movie[1]}: ")
                                movie[2] = int(input(f"Masukkan jumlah tiket baru untuk film {movie[1]}: "))
                                movie[3] = int(input(f"Masukkan harga tiket baru untuk film {movie[1]}: "))
                                print(f"Film dengan ID {id_film} berhasil diupdate.")
                                break
                        else:
                            print(f"Film dengan ID {id_film} tidak ditemukan.")

                    elif admin_choice == 4:
                        print("\n==== Hapus Film ====")
                        id_film = int(input("Masukkan ID film yang ingin dihapus: "))
                        for movie in movies:
                            if movie[0] == id_film:
                                movies.remove(movie)
                                print(f"Film dengan ID {id_film} berhasil dihapus.")
                                break
                        else:
                            print(f"Film dengan ID {id_film} tidak ditemukan.")

                    elif admin_choice == 5:
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid.")

            elif logged_in_user[2] == "pengguna":
                
                while True:
                    print("""
==========================================
|              Sistem Pengguna           |
==========================================
|              1. Lihat Film             |
|              2. Beli Tiket             |
|              3. Lihat Registrasi       |
|              4. LogOut                 |
==========================================

""")
                    pilih = int(input("Pilih opsi: "))

                    if pilih == 1:
                        print("\n==== Daftar Film ====")
                        for movie in movies:
                            print(f"ID: {movie[0]}, Judul: {movie[1]}, Sisa Tiket: {movie[2]}, Harga Tiket: {movie[3]}")

                    elif pilih == 2:
                        print("\n==== Beli Tiket ====")
                        id_film = int(input("Masukkan ID film yang ingin dibeli: "))
                        jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))

                        for movie in movies:
                            if movie[0] == id_film:
                                    if movie[2] >= jumlah_tiket:
                                        total_harga = jumlah_tiket * movie[3]
                                        movie[2] -= jumlah_tiket
                                        transactions.append([logged_in_user[0], id_film, jumlah_tiket, total_harga])
                                        print(f"Pembelian {jumlah_tiket} tiket berhasil untuk film {movie[1]}. Total harga: Rp{total_harga}")
                                    else:
                                        print("Tiket tidak tersedia.")
                                    break
                            else:
                                print(f"Id film tidak ditemukan.")
                                
                    
                    
                    elif pilih == 3:
                        print("\n===== Lihat Registrasi ====")
                        for transaction in transactions:
                            if transaction[0] == logged_in_user[0]:
                                print(f"Username: {transaction[0]}, ID Film: {transaction[1]}, Jumlah Tiket: {transaction[2]}, Total Harga: Rp{transaction[3]}")
                    
                    elif pilih == 4:
                        Logout = input("apakah kamu yakin ingin keluar dari aplikasi (ya/tidak): ")
                        print("Logout berhasil.Terimakasih telah menggunakan sistem ini")
                    logged_in_user = None
                    break
                
        elif pilih == 3:
            print("Anda keluar dari aplikasi")
            break
        else:
            print("Pilihan tidak valid.")

    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
