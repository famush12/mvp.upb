def find_largest_number():
    largest = float('-inf')  # Inisialisasi dengan nilai negatif tak terhingga
    count = 0

    while True:
        num = float(input(f"Masukkan bilangan ke-{count + 1} (atau 0 untuk selesai): "))
        
        if num == 0:
            break
        
        count += 1
        
        if num > largest:
            largest = num

    return largest, count

# Menjalankan program
print("Program untuk menentukan bilangan terbesar dari N bilangan")
print("Masukkan angka 0 untuk mengakhiri input\n")

largest, count = find_largest_number()

if count > 0:
    print(f"\nJumlah bilangan yang dimasukkan: {count}")
    print(f"Bilangan terbesar adalah: {largest}")
else:
    print("\nTidak ada bilangan yang dimasukkan.")
