#r,c ukuran map, N banyak siswa
N, r, c = map(int, input().split())
posisi_siswa = []

for i in range(N):
    xi, ai, bi = map(int, input().split())
    posisi_siswa.append((xi, ai, bi))  # Memasukkan data siswa ke dalam list sebagai tuple

# posisi siswa apakah bersebelahan
for j in range(1,N + 1):
    ada = False
    for siswa in posisi_siswa:
        nomor, ai, bi = siswa
        if nomor == j:
            # Cek posisi kiri
            for s in posisi_siswa:
                if s[1] == ai and s[2] == bi - 1:
                    print(s[0])  
                    ada = True
                    break  
            # Cek posisi kanan
            for s in posisi_siswa:
                if s[1] == ai and s[2] == bi + 1:
                    print(s[0])  
                    ada = True
                    break  
            break 
    #jika tidak ada, cetak 0
    if not ada:
        print(0)  

#xi =nomor urut
#ai =baris
#bi =kolom

