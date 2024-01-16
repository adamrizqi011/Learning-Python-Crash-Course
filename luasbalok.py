print ('Print menghitung luas balok :')
print ('=============================')
print()

panjang = float(input('Panjang balok :'))
lebar = float(input('Lebar balok :'))
tinggi = float(input('Tinggi Balok :'))

luas = 2*(panjang*lebar) + 2*(panjang*tinggi) + 2*(lebar*tinggi)
 
print('Luas permukaan balok = ',round(luas,2))