angka = int(input("Masukkan angka ganjil: "))
if angka % 2 == 0:
    print("Angka genap tak bolehlah")
else:
    for i in range(angka // 2 + 1):
        print(" " * i + "*" * (angka - i * 2), end=" ")
        print()

    for i in range(angka // 2 - 1, -1, -1):
        print(" " * i  + "*" * (angka - i * 2), end=" ")
        print()
