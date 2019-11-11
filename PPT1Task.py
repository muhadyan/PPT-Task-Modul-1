
# Solve it! 2
kuadrat = int(input('Silahkan masukan angka berapapun : '))
hasil = kuadrat ** 2
print('Hasil dari Kuadrat ', kuadrat, 'adalah', hasil)



#Solve it! 3
import math

case = 485

year = (case/360)
yearfloor = math.floor(year)
month = ((year-yearfloor)*360)/30
monthfloor = math.floor(month)
week = ((month-monthfloor)*30)/7
weekfloor = math.floor(week)
day = ((week-weekfloor)*7)
dayfloor = math.floor(day)

print('Jadi,', case, 'hari sama dengan', yearfloor, 'Tahun,', monthfloor, 'Bulan,', weekfloor, 'Minggu,', dayfloor, 'Hari')



# Solve it! 4
rasio = 2/5
TotUmur = 49
x = 2

Andi = int(rasio*TotUmur)
Budi = int((1-rasio)*TotUmur)

print('Jadi,', x, 'tahun lagi umur Andi adalah', x+Andi, 'Tahun dan Budi adalah', x+Budi, 'Tahun')



# Solve it! 5
text = "'Kuku kakiku sungguh kaku sekali'"
case = 'k'

x = text.lower()
y = x.replace(case, '')
z = len(x)-len(y)

print('Jumlah huruf', case, 'pada kalimat', text, 'ada', z, 'huruf')



#Solve it! 6
import math

TotJarak = 120
A = 60
B = 40
start = 9

x = ((TotJarak/(A+B))*60)
y = math.floor(x/60)
z = int(x%60)

print(f'Mobil A dan B akan bertabrakan pada jam {start+y}.{z}')
