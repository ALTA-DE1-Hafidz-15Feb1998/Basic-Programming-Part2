'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''
# Input
harga = 370000
diskon = 15
harga_diskon = diskon / 100 * harga
harga_akhir = harga - harga_diskon

# Output
print ("Harga yang harus dibayar adalah Rp." , harga_akhir)