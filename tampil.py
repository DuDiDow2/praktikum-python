from rich.console import Console
from rich.table import Table
console = Console()
tabel = Table(title="Daftar Alat Praktikum")
tabel.add_column("No", justify="right")
tabel.add_column("Alat")
tabel.add_column("Fungsi")
tabel.add_row("1", "VS Code", "Menulis dan menjalankan kode")
tabel.add_row("2", "venv", "Mengisolasi paket proyek")
tabel.add_row("3", "Git", "Mencatat riwayat perubahan")
console.print(tabel)