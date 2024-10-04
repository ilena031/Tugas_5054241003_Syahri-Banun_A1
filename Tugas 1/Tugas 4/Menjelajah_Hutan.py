#r, c besar map dan N 
r,c,N = map (int,input ().split ())
#buat 2d list
Aij = [list (map (int,input ().split()))for i in range (r)]
#pisah 2dlist menjadi baris & kolom 
i,j = 0,0 
gold = Aij[i][j] 
Aij[i][j] = 0 
#gerakan 
gerakan = input ()
for arah in gerakan : 
    if arah == 'U' and i >0  : 
        i-=1
        gold +=3
    elif arah == 'D' and i-1<r: 
        i+= 1
        gold -= 2
    elif arah == 'R' and j-1<c : 
        j+= 1
        gold += 3
    elif arah == 'L' and j>0 : 
        j-=1 
        gold -=2 
    else : 
        print ("gerakanmu salah bung!")
        break
#tambhkan gold yang di dalam array 
    gold+= Aij[i][j]
print ("total emas yang didapat adalah",gold)
        
#input 
#4 4 5
#1 1 1 2
#2 2 3 1
#3 4 5 7
#7 2 2 2
#RDLLLU

