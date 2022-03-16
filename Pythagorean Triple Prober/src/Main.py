# Penyelidik Bilangan Tripel Pythagoras

print("Penyelidik Bilangan Tripel Pythagoras\r\nVersi: 1.0\r\nOleh: Ernest Noell\r\n")

# Nilai a
a = float(input("Ketikkan panjang sisi a (hipotenusa/sisi miring segitiga/sisi terpanjang): "))
print(f"Nilai a yang telah dimasukkan: {a}")

# Nilai b
b = float(input("Ketikkan panjang sisi b (sisi samping/sisi tegak): "))
print(f"Nilai b yang telah dimasukkan: {b}")

# Nilai c
c = float(input("Ketikkan panjang sisi c (sisi depan/sisi datar): "))
print(f"Nilai c yang telah dimasukkan: {c}")


a_ruasKiri = a ** 2.0
a_ruasKanan = b ** 2.0 + c ** 2.0


if a_ruasKiri == a_ruasKanan: hasil = "Ketiga bilangan merupakan Tripel Pythagoras (segitiga siku-siku)."
elif a_ruasKiri > a_ruasKanan: hasil = "Ketiga bilangan bukan merupakan Tripel Pythagoras (segitiga tumpul)."
else: hasil = "Ketiga bilangan bukan merupakan Tripel Pythagoras (segitiga lancip)."

print(hasil)


print("Pythagorean Triple Probrer is shutting down...")