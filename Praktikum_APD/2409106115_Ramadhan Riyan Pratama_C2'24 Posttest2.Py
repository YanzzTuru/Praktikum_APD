nama = input("Masukkan nama Anda: ")
nim = input("Masukkan NIM Anda: ")

harga_tesla = float(input("Masukkan harga mobil Tesla: "))
diskon_tesla = 0.17
harga_tesla_setelah_diskon = harga_tesla * (1 - diskon_tesla)
modulus_7_tesla = harga_tesla % 7

harga_toyota = float(input("Masukkan harga mobil Toyota: "))
diskon_toyota = 0.21
harga_toyota_setelah_diskon = harga_toyota * (1 - diskon_toyota)
modulus_7_toyota = harga_toyota % 7

harga_hyundai = float(input("Masukkan harga mobil Hyundai: "))
diskon_hyundai = 0.23
harga_hyundai_setelah_diskon = harga_hyundai * (1 - diskon_hyundai)
modulus_7_hyundai = harga_hyundai % 7



print(f"Mobil Tesla seharga {harga_tesla} diskon 17% menjadi {harga_tesla_setelah_diskon:.2f}, "
      f"Mobil Toyota seharga {harga_toyota} diskon 21% menjadi {harga_toyota_setelah_diskon:.2f}, "
      f"Mobil Hyundai seharga {harga_hyundai} diskon 23% menjadi {harga_hyundai_setelah_diskon:.2f}.")
print(f"Modulus 7 dari harga Tesla adalah {modulus_7_tesla:.2f}, "
      f"modulus 7 dari harga Toyota adalah {modulus_7_toyota:.2f}, "
      f"dan modulus 7 dari harga Hyundai adalah {modulus_7_hyundai:.2f}.")