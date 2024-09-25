ulang = 10
for i in range(ulang):
    print("perulangan ke-" + str(i))

for i in range(2,10):
    print(f"halo {i}")

for i in range(2,10,2):
    print(f"halo {i}")
    
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
    print(f"Total perulangan: {hitung}")

while True:
    print("hallo")

hitung = 0
while True:
    hitung += 1
    ulang = input("Masih Ingin Mengulang? ")
    if ulang == "tidak" or ulang =="Tidak":
        break

print(f"Total Perulangan: {hitung}")

while True:
    print("hallo")
    break

while True:
    print("hallo")
    print("fufufafa")
    continue

print('Daftar bilangan ganjil 1-10')
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print('Daftar bilangan genap 1-10')
for i in range(1,11):
    if i % 2 != 0:
        continue
    print(i)

kelasC = ["riyan",2409106115]

for i in range(len(kelasC)):
    print(f"{i+1}, {kelasC[i]}")
print(kelasC)
