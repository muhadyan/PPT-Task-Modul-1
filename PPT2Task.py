# Solve it 1!
x = int(input('Masukan angka berapa saja: '))

if x % 2 == 0:
    print(f'Angka {x} adalah bilangan GENAP')
else:
    print(f'Angka {x} adalah bilangan GANJIL')



# Solve it 2!
massa = int(input('Masukkan berat badan Anda (kg): '))
tinggi = int(input('Masukkan tinggan badan Anda (cm): '))

IMT = massa/((tinggi/100)**2)

if IMT < 18.5:
    print('Berat Badan Anda KURANG')
elif 18.5 <= IMT < 25:
    print('Berat Badan Anda IDEAL')
elif 25 <= IMT < 30:
    print('Berat Badan Anda BERLEBIH')
elif 30 <= IMT < 40:
    print('Berat Badan Anda SANGAT BERLEBIH')
else:
    print('Berat Badan Anda OBESITAS')