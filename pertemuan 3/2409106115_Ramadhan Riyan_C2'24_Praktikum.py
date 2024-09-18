cuaca= "mendung"

if cuaca == "mendung":
	print ("diam di rumah")
else:
	print("hari ini mendung")

Umur = int(input("masukan umur anda"))
if Umur > 0:
	if Umur <= 10:
			print("umur anda termasuk kategori anak-anak")
	elif Umur <= 18:
		print("umur anda termasuk kategori remaja")
	elif Umur <=35:
		print("umur anda termasuk kategori dewasa")
	elif Umur <=65:
		print("umur anda termasuk lategori paruh baya")
	else:
		print("umur anda termasuk tua")

else:
	print("input usia harus bilangan positif")

nim = int(input("masukan nim: "))
if nim >= 1 and nim <= 50 :
	if nim >= 1 and nim <= 25 :
		print("Kelas A'1")
	else:
		print("Kelas A'2")
elif nim >= 52 and nim<= 100:
	if nim >=51 and nim <= 75 :
		print("Kelas B'1")
	else:
		print("Kelas b'2")
elif nim >= 101 and nim <= 121 :
	if nim >= 101 and nim <= 110 :
		print("Kelas C'1")
	else:
		print("kelas C'2")
else:
	print("anda bukan mahasiswa informatika 24")
