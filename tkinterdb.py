import tkinter as tk
import sqlite3

def hasil_prediksi():
    # Mendapatkan nilai dari slider
    nilai_mata_pelajaran = [slider.get() for slider in sliders]

    # Mendapatkan nilai dari entry nama siswa
    nama_siswa = entry_nama.get()

    # Mendefinisikan mata pelajaran dan program studi terkait
    mata_pelajaran = ["Matematika", "Fisika", "Kimia", "Biologi", "Bahasa Inggris",
                      "Bahasa Indonesia", "Ekonomi", "Sejarah", "Geografi", "Seni"]
    prodi_terpilih = ""

    # Menentukan hasil prediksi berdasarkan nilai tertinggi
    max_nilai = max(nilai_mata_pelajaran)
    max_index = nilai_mata_pelajaran.index(max_nilai)

    if mata_pelajaran[max_index] == "Matematika":
        prodi_terpilih = "Ilmu Matematika"
    elif mata_pelajaran[max_index] == "Fisika":
        prodi_terpilih = "Astronomi"
    elif mata_pelajaran[max_index] == "Kimia":
        prodi_terpilih = "Teknik Kimia"
    elif mata_pelajaran[max_index] == "Biologi":
        prodi_terpilih = "Kedokteran"
    elif mata_pelajaran[max_index] == "Bahasa Inggris":
        prodi_terpilih = "Sastra Inggris"
    elif mata_pelajaran[max_index] == "Bahasa Indonesia":
        prodi_terpilih = "Sastra Indonesia"
    elif mata_pelajaran[max_index] == "Ekonomi":
        prodi_terpilih = "Ilmu Ekonomi"
    elif mata_pelajaran[max_index] == "Sejarah":
        prodi_terpilih = "Ilmu Sejarah"
    elif mata_pelajaran[max_index] == "Geografi":
        prodi_terpilih = "Meteorologi"
    elif mata_pelajaran[max_index] == "Seni":
        prodi_terpilih = "Ilmu Seni"

    # Menampilkan hasil prediksi pada label
    hasil_label.config(text=f"Hasil Prediksi untuk {nama_siswa}: {prodi_terpilih}")

    # Menyimpan data ke database SQLite
    simpan_data_ke_sqlite(nilai_mata_pelajaran[0], nilai_mata_pelajaran[1], nilai_mata_pelajaran[2], nilai_mata_pelajaran[3], nilai_mata_pelajaran[4], nilai_mata_pelajaran[5], nilai_mata_pelajaran[6], nilai_mata_pelajaran[7], nilai_mata_pelajaran[8], nilai_mata_pelajaran[9],prodi_terpilih)

def simpan_data_ke_sqlite(matematika, fisika, kimia, biologi, inggris, indonesia, ekonomi, sejarah, geografi, seni, prodi_terpilih):
    # Membuka atau membuat database SQLite
    conn = sqlite3.connect("prodidb.db")
    cursor = conn.cursor()

    # Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    matematika INTEGER, 
                    fisika INTEGER,
                    kimia INTEGER,
                    biologi INTEGER,
                    inggris INTEGER,
                    indonesia INTEGER,
                    ekonomi INTEGER,
                    sejarah INTEGER,
                    geografi INTEGER,
                    seni INTEGER,
                    prodi_terpilih TEXT)''')

    # Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute("INSERT INTO hasil_prediksi (matematika, fisika, kimia, biologi, inggris, indonesia, ekonomi, sejarah, geografi, seni, prodi_terpilih) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (matematika, fisika, kimia, biologi, inggris, indonesia, ekonomi, sejarah, geografi, seni, prodi_terpilih))

    # Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()

# Membuat instance Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Label judul Aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Helvetica", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Input nama siswa
label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.grid(row=11, column=0, padx=10, pady=5, sticky="e")

entry_nama = tk.Entry(root)
entry_nama.grid(row=11, column=1, padx=10, pady=5)

# Slider nilai mata pelajaran
mata_pelajaran_labels = ["Matematika", "Fisika", "Kimia", "Biologi", "Bahasa Inggris",
                         "Bahasa Indonesia", "Ekonomi", "Sejarah", "Geografi", "Seni"]
sliders = []

for i, label_text in enumerate(mata_pelajaran_labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="e")

    slider = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200)
    slider.grid(row=i + 1, column=1, padx=10, pady=5)
    sliders.append(slider)

# Button Hasil Prediksi
button_prediksi = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
button_prediksi.grid(row=12, column=0, columnspan=2, pady=10)

# Label luaran hasil prediksi
hasil_label = tk.Label(root, text="Hasil Prediksi: ")
hasil_label.grid(row=13, column=0, columnspan=2, pady=10)

# Menjalankan GUI
root.mainloop()