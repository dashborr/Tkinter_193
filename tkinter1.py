import tkinter as tk

# ---------- Fungsi ----------
def hasil_prediksi():
    # Apapun input yang diberikan, hasilnya selalu Teknologi Informasi
    label_hasil.config(text="Teknologi Informasi")

# ---------- Jendela utama ----------
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.resizable(False, False)

# Posisikan jendela di tengah layar
lebar, tinggi = 560, 520
x = (root.winfo_screenwidth() - lebar) // 2
y = (root.winfo_screenheight() - tinggi) // 2
root.geometry(f"{lebar}x{tinggi}+{x}+{y}")

# ---------- Label judul ----------
label_judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold"),
    fg="#1a3c6e",
)
label_judul.pack(pady=(25, 15))

# ---------- Frame input (10 nilai mapel, 2 kolom x 5 baris) ----------
frame_input = tk.LabelFrame(
    root, text=" Masukkan Nilai Mata Pelajaran ", font=("Arial", 11), padx=20, pady=15
)
frame_input.pack(padx=30, pady=10)

mapel = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Geografi", "Sosiologi", "Sejarah",
]