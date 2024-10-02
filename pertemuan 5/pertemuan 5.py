nama = ["shandy",106,True,
       ["yuyun",145],3.96
       [123,"ALVITO",False,3.66],
       "rehan"]

print(nama[4])

matkul = ["APD",
          "APL",
          "WEB",
          "JARKOM",
          "BASDAT",
          "STRUKDAT",
          "PTI",
          "KALKULUS",
          "PROBAS"]

print(nama[1])


makanan = ["Bakso","Sate","Soto","Nasi Goreng","Mie Goreng","Cumi Goreng"]
print("Sebelum; ")
print(makanan[2:5])
makanan.append("Nasi Goreng")
print("Sesudah")
del makanan[2]
print(makanan)
data = makanan.pop(5)
print(data)
makanan.clear()
print(makanan)
makanan.insert(2,"Nasi Goreng")
print(makanan)
makanan[0] = ["Ayam","Bebek"]
print(makanan)


minuman = ["es teh","jus","milo","alpukat","mangga","taro"]
print("sebelum")
print(minuman)
del minuman[3]
print(minuman)
minuman[4] = "air putih"
minuman.insert(0,"es teler")
print(minuman)

makanan = ["ayam","ikan"],["bakso","soto","sate","ikan","bebe"],["teh","kopi","air"]

for i in makanan :
    if isinstance(i, list):
        for j in i :
            print(j)
        
    else :
        print(i)

for i in makanan :
    if isinstance(i, list):
        for j in i :
            print(j)
        
   
akuns = []

while True:
    print("Hallo!selamat datang diaplikasi Catatan")
    print("Silahkan pilih'Daftar akun'Jika belum buat akun,dan jika sudah memiliki akun silahkan'Login'")
    print("1. Daftar Akun")
    print("2. Login")
    print("3. Exit")
    print("______________")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Hallo Pengguna baru!Ayo buat akun dulu")
        username = input("username:")
        akuna = False
        for akun in akuns:
            if akun[0] == username:
                akuna = True
                break
        if akuna:
            print("Nama sudah terpakai untuk registrasi silahkan coba lagi")
        else:
            Password = input("Password: ")
            akuns.append([username,Password,])
            print(f"Akun anda berhasil terdaftar dengan ID: {username}")

    
