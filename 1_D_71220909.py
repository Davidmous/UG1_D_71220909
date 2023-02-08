harga = int(input('Harga Barang : '))
beli = input('Apakah anda membeli barang lagi? [Yes/No] : ')

while True :
    if beli == 'Yes' :
        harga2 = int(input('Harga Barang : '))
        beli = input('Apakah anda membeli barang lagi? [Yes/No] : ')
        harga += harga2
    elif beli == 'No' :
        print('TOTAL BELANJA : ', harga)
        break
    else :
        print('INVALID')
        break
         




