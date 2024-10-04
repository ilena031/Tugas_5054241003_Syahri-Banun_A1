n = int (input ("input G's n number here : "))
#cetak angka yang sudah tidak mungkin prima (negatif dan 1)
if n <= 1 : print ("IT IS NOT A PRIME")
#untuk angka 2 dan 3 sudah pasti prima
elif n<=3 : print ("IT IS A PRIME")
#untuk angka yang habis dibagi 2 dan 3 sudah pasti bukan prima
elif n%2 == 0 or n%3 ==0 : print ("IT IS NOT A PRIME")
else : 
    #variabel digunakan untuk mendiclare apa code tersebut bernilai benar atau salah 
    is_prime = True
    #menggunakan 5 karena, 5 adalah bilangan prima paling kecil setelah 2 dan 3, maka agar tidak banyak if else gunakan 5
    i = 5
    #looping diperlukan karena interval angka hingga 1000
    while i*i <= n : 
        #apabila angka habis dibagi dengan fungsi i, maka bukan prima
        if n % i ==0 or n%(i+2)== 0 : 
            is_prime = False 
    i+= 6
    if is_prime : print ("IT IS A PRIME")
    else : print ("IT IS A NOT PRIME")