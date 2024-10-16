# def mhs ():
#     print("Hello")

# mhs()

# def kali ():
#     x = 6*4
#     print(x)

# kali()


# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print ("Luas persegi panjang:", luas)
#     print(f"Luas persegi panjang: {luas} cm ")

# luas_persegi_panjang(10, 6)


# def luas_persegi(sisi):
#     luas = sisi*sisi
#     jumlah = sisi+sisi
#     return luas, jumlah

# luas, jumlahn = luas_persegi(2)
# hasil = luas_persegi(4)+luas_persegi(2)
# print(hasil)

# def mhs(nama,nim, *arr):
#     print(nama)
#     print(nim)
#     print(arr)

# mhs("ucup", "20", data = 2, data2 = 3)

# def nilai (angka):
#     if angka >10:
#         print(1)
#         return
#     else :
#         print(2)
#         return
#     print("3")

# nilai(10)

# def nilai ():
#     data = 20
#     print(data)
    
# print(nilai)\

# def data(kumpulan):
#     print(kumpulan)

# value = [1,2,3,4]
# data(value)

# def mhs(nama1, nama2, nama3):
#     print(nama3)

# mhs(nama3= "ucup", nama2= "saipul", nama1= "michel")

# import os

# data_mahasiswa = [
#     {
#         "Nama": "Andi",
#         "Nim": "123"
#     },
#     {
#         "Nama": "Budi",
#         "Nim": "124"
#     },
#     {
#         "Nama": "Ucup",
#         "Nim": "125"
#     }
# ]

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def lihat_data():
#     print("===Lihat Data===")
#     for i, mahasiswa in enumerate(data_mahasiswa, start=1):
#         print(f"Data ke {i}")
#         print(f"Nama : {mahasiswa['Nama']}")
#         print(f"Nim : {mahasiswa['Nim']}")
#         print("=" * 10)
#     input("Enter untuk kembali...")

# def tambah_data():
#     print("== Tambah Data ==")
#     input_nama = input("Nama\t: ")
#     input_nim = input("Nim\t: ")
#     data_mahasiswa.append({
#         "Nama": input_nama,
#         "Nim": input_nim
#     })
#     print(f"{input_nama} dengan NIM {input_nim} telah ditambahkan")
#     input("Enter untuk kembali...")

# def edit_data():
#     print("== Ubah Data ==")
#     lihat_data()
#     try:
#         index = int(input("Masukkan nomor data yang mau diedit: "))
#         if 0 < index <= len(data_mahasiswa):
#             nama_baru = input("Masukkan nama baru: ")
#             nim_baru = input("Masukkan NIM baru: ")
#             data_mahasiswa[index-1]["Nama"] = nama_baru
#             data_mahasiswa[index-1]["Nim"] = nim_baru
#             print("Data berhasil diubah")
#         else:
#             print("Index tidak ditemukan")
#     except ValueError:
#         print("Input tidak valid")
#     input("Enter untuk kembali...")

# def hapus_data():
#     print("== Hapus Data ==")
#     lihat_data()
#     try:
#         index = int(input("Masukkan nomor data yang ingin dihapus: "))
#         if 0 < index <= len(data_mahasiswa):
#             del_data = data_mahasiswa.pop(index-1)
#             print(f"{del_data['Nama']} dengan NIM {del_data['Nim']} telah dihapus")
#         else:
#             print("Index tidak ditemukan")
#     except ValueError:
#         print("Input tidak valid")
#     input("Enter untuk kembali...")

# def menu():
#     while True:
#         clear_screen()
#         print("""
#         Menu
#         Lihat Data  >> 1
#         Tambah Data >> 2
#         Edit Data   >> 3
#         Hapus Data  >> 4
#         Keluar      >> 5
#         """)
#         pilih = input("Masukkan pilihan menu >> ")
#         clear_screen()
#         match pilih:
#             case "1":
#                 lihat_data()
#             case "2":
#                 tambah_data()
#             case "3":
#                 edit_data()
#             case "4":
#                 hapus_data()
#             case "5":
#                 print("Bye bye")
#                 break
#             case _:
#                 print(f"Menu {pilih} tidak tersedia")
#                 input("Enter untuk kembali...")

# if __name__== "_main_":
#     os.system