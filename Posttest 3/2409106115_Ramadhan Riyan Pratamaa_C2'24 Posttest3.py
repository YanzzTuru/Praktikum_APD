harga_mobil= float(input("Masukkan harga mobil: "))

print("Pilih merk mobil yang ingin dibeli:")
print("1. Tesla")
print("2. Toyota")
print("3. Hyundai")
print("4. Tidak membeli mobil")
pilihan = int(input("Masukkan nomor pilihan merk mobil: "))

if pilihan == 1:
    diskon = 17/100 * harga_mobil
    harga_setelah_diskon = harga_mobil - diskon
    print(f"Merk Mobil: Tesla, Diskon: 17%, Harga setelah diskon: {harga_setelah_diskon}")
elif pilihan == 2:
    diskon = 21/100 * harga_mobil
    harga_setelah_diskon = harga_mobil - diskon
    print(f"Merk Mobil: Toyota, Diskon: 21%, Harga setelah diskon: {harga_setelah_diskon}")
elif pilihan == 3:
    diskon = 23/100 * harga_mobil
    harga_setelah_diskon = harga_mobil - diskon
    print(f"Merk Mobil: Hyundai, Diskon: 23%, Harga setelah diskon: {harga_setelah_diskon}")
elif pilihan == 4:
    print("Bu Navira tidak jadi membeli mobil.")
else:
    print("tidak jadi beli wak")

