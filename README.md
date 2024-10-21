Membuat Kode Program dari flowchart pertemuan ke 5
Tugas Pertemuan Ke 5

Nama: fawaidil mustofa

Kelas: TI 24 A3

NIM: 312410433

1. bilanganterbesar.py
Program pertama yang akan dibuat adalah Program untuk menampilkan bilangan terbesar dari 3 Bilangan yang di Inputkan

Berikut flowchartnya

Flowchart

Program akan meminta kita untuk memasukkan 3 angka untuk dibandingkan :

output

Penjelasan Code

1.

def mencari_bilangan_terbesar(a, b, c):
    if a > b:
        if a > c:
            return a, "A adalah terbesar"
        else:
            return c, "C adalah terbesar"
    else:
        if b > c:
            return b, "B adalah terbesar"
        else:
            return c, "C adalah terbesar"

# Input bilangan A, B, C
print("Masukkan tiga bilangan:")
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

# Menentukan bilangan terbesar
largest, message = mencari_bilangan_terbesar(a, b, c)

# Menampilkan hasil
print(f"\n{message}")
print(f"Bilangan terbesar adalah: {largest}")
Kita mendefinisikan function mencari_bilangan_terbesar yang mengambil tiga parameter (a,b,c).
function tersebut menggunakan nested if-else statement untuk membandingkan angka yang di inputkan
Kemudian akan menampilkan Mana bilangan terbesar
Lalu di Program utamanya kita masukkan angka yang harus dimasukkan oleh user
Lalu kita panggil kembali function mencari_biilangan_terbesar
Lalu Output bilangan terbesar dari ketiga bilangan yang di input akan muncul
2. bilanganN.py
Program Kedua adalah untuk membandingkan bilangan yang di Input, input akan terus berjalan kecuali user memasukkan nilai 0

Flowchartnya

Flowchart

Program akan meminta kita untuk memasukkan angka untuk dibandingkan, `input akan terus diminta sebelum user memasukkan angka 0 :

output

Penjelasan Code

def find_largest_number():
Mendefinisikan fungsi bernama find_largest_number yang akan menangani logika utama program.

    largest = float('-inf')  # Inisialisasi dengan nilai negatif tak terhingga
Menginisialisasi variabel largest dengan nilai negatif tak terhingga. Ini memastikan bahwa angka pertama yang dimasukkan akan selalu lebih besar.

*Maksud dari -infinity(Negatif tak hingga) adalah nilai negatif berapapun.

    count = 0
Menginisialisasi variabel count untuk menghitung jumlah bilangan yang dimasukkan.

    while True:
Memulai loop tak terbatas. Akan terus berjalan sampai dihentikan oleh break.

        num = float(input(f"Masukkan bilangan ke-{count + 1} (atau 0 untuk selesai): "))

Meminta input dari pengguna, mengkonversinya ke float, dan menyimpannya dalam variabel num.

if num == 0:
            break
Jika input adalah 0, keluar dari loop.

count += 1
Menambah penghitung jumlah bilangan yang dimasukkan.

if num > largest:
            largest = num
Jika bilangan yang baru dimasukkan lebih besar dari largest saat ini, update largest.

return largest, count
Setelah loop selesai, kembalikan bilangan terbesar dan jumlah input.

print("Program untuk menentukan bilangan terbesar dari N bilangan")
print("Masukkan angka 0 untuk mengakhiri input\n")
Mencetak instruksi untuk pengguna.

largest, count = find_largest_number()
Memanggil fungsi find_largest_number() dan menyimpan hasilnya.

if count > 0:
Memeriksa apakah ada bilangan yang dimasukkan.

print(f"\nJumlah bilangan yang dimasukkan: {count}")
    print(f"Bilangan terbesar adalah: {largest}")
Jika ada bilangan yang dimasukkan, cetak jumlah input dan bilangan terbesar.

else:
    print("\nTidak ada bilangan yang dimasukkan.")
Jika tidak ada bilangan yang dimasukkan (pengguna langsung memasukkan 0), program akan dijalankan dan menampilkan output perbandingan.
