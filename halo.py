# halo.py - program Python pertama
from datetime import date

nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}! Selamat datang di praktikum Python.")

while True:
    try:
        tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
        tahun_ini = date.today().year
        if tahun_lahir > tahun_ini or tahun_lahir < 1900:
            print("Tahun lahir tidak masuk akal, coba lagi.")
            continue
        break
    except ValueError:
        print("Input harus berupa angka, coba lagi.")

usia = date.today().year - tahun_lahir
print(f"Perkiraan usia Anda saat ini: {usia} tahun.")
print("Semoga sukses!")