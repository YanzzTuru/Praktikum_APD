# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])
# print(daftar_buku)


# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#     "Instagram" : "@aldyrmdhns_",
#     "Discord" : "\'Izanami#6848",
#     "Email" : "iniemail@gmail.com"
#     }
# }

# print(Biodata["KRS"][0])
# print(Biodata["Social Media"]["Email"])


# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = {"nama" : {123 : "informatika"}} )
# print(games['Valorant']['nama'][123])

# Games = {
#     "Game1" : "PUBG MObile",
#     "Game2" : "Mobile Legend",
#     "Game3" : {
#         "nama" : "COC",
#         "genre" :"Strategy"
# }
# }
# print((Games.get('Game3')).get('genre'))

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# #tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")

# #menggunakan items
# for mapel, Nilai in Nilai.items():
#     print(f"Nilai {mapel} anda adalah {Nilai}")

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }

# #Sebelum Ditambah
# print(Film)
# ']'
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller","Rush Hour" : "Comedy", "Oblivion" : "Science Fiction"})

# #Setelah Ditambah

# del Film["Avenger Endgame"]
# print(Film)

# simpan = Film.pop('Hours')
# Film.clear()
# print(Film)
# Film["Hours"] = simpan
# print(Film)

# movies = Film.copy()
# print(movies)
# print("Jumlah Film =  ", len(movies))

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai kimia : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
# "The Chainsmoker" : ["All we Know", "TheParis"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
# for song in j:
#     print(song)
# print("")


# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
# for x, y  in value.items():
#     print (x, " : ", y)
# print("")


angkatan = {
    "nama" :"riyan",
    "umur" : "18",
    "nim" : "2409106115",
    "jurusan" : "Informatika",
    "angkatan" : "24"

}

print(angkatan)
angkatan["fakultas"] = input("masukan fakultas :")
print(angkatan)
ubah = input("ubay key")
angkatan[ubah] = input("velue baru")
print(angkatan)
hapus = input("hapus velue:")
del angkatan[hapus]
print(angkatan)


nilai = {
"matematika" : 90,
"fisika" : 80,
"biologi" : 80,
"kimia" : 70

}
total = 0
for i in nilai.velues():
    total += i
print(f"total nilai adalah {total}")
print(f"rata rata adalah {total/4}")

