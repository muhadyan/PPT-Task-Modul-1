# Solve it! 1
# Buatlah aplikasi python sederhana untuk filtering list (searching) berdasarkan input user
listNya = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari ayam']
listNyo = []
x = input('Cari: ')
x.upper()
for i in listNya:
    a = i.upper()
    listNyo.append(a)
y = list(filter(lambda a : x.upper() in a, listNyo))
listnyau = []
for i in y:
    b = listNyo.index(i)
    c = listNya[b]
    listnyau.append(c)
print(listnyau)