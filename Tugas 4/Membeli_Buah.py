#N ragam buah, K uang yang dimiliki 
N, K = map (int,input ().split ())
#harga dari ragma buah
Ai = list(map(int, input ().split ()))
count = 0
array_buah = []
#looping nilai buah
for i in range (N): 
    if Ai [i] <= K: #ketika K lebih besar dari Ai maka akan bertambah 1 perhtungna
        count += 1
        array_buah.append (i+1)
#membuat output
buah_ke = ', '.join(['buah ke-',j for j in array_buah[:-1]]) + ', dan buah ke-',array_buah[-1]
print (count)
print ("Dengan uang", K ,"ia bisa membeli dengan kemungkinan", count, "jenis buah yaitu ",buah_ke)


#input 
#5 1000
#1000 2000 500 400 3000