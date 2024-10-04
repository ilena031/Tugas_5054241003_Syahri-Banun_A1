#N banyak barang, M banyak uang yang diberkan
N, M = map (int,input ().split ())
uang = []
harga = []

#looping nilai barang yang psotif
Pi = list (map (int, input ().split ()))
for i in Pi : 
    if i > 0 : 
        (uang.append (i))
        break
    else : 
        (uang.append (max(Pi)))
#looping uang yang negatif
Cj = list (map (int,input ().split()))
for j in Cj : 
    if j < 0 : 
        (harga.append (j))
        break
    else : 
        (harga.append (min(Cj)))
        

harga = sum (harga)
uang = sum (uang)
print (harga - uang)





