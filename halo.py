# halo.py - program Python pertama
from datetime import date
from colorama import init, Fore, Style

init(autoreset=True)

nama = input("Masukkan nama Anda: ")
print(Fore.GREEN + f"Halo, {nama}! Selamat datang di praktikum Python.")

while True:
    try:
        tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
        tahun_ini = date.today().year
        if tahun_lahir > tahun_ini or tahun_lahir < 1900:
            print(Fore.YELLOW + "Tahun lahir tidak masuk akal, coba lagi.")
            continue
        break
    except ValueError:
        print(Fore.RED + "Input harus berupa angka, coba lagi.")

usia = date.today().year - tahun_lahir
print(Fore.CYAN + Style.BRIGHT + f"Perkiraan usia Anda saat ini: {usia} tahun.")
print(Fore.GREEN + "Semoga sukses!")