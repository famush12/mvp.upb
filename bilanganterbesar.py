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
