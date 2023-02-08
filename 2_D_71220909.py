teliti = input('Kalimat yang ingin diteliti : ').split()
dicari = input('Kata yang dicari : ')
j = 0

for i in list(teliti) :
    if i == dicari:
        j = j + 1
print('Jumlah kata yang dicari : ', j)