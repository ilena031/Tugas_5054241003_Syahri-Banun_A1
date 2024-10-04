NumList = list(map (int,input("7 Number that witch given is : ") .split()))
AmountJump = int (input ("Amount of cats will jump from back to the front : "))
Repetition = int (input ("How many times the repetition? "))
Index = list(map (int, input ("Three Index you want to print : ").split ()))

#function ini berguna untuk looping kode hingga angka yang terlah ditetapkan user
for i in range (Repetition) : 
    #[:-x] untuk mengambil angka awal dari numlist sedgnkn [-x:] berguan untuk mengmbl angka akhir
    NumList =  NumList[-AmountJump:] + NumList[:-AmountJump]
#untuk mengambil angka yang di tentukan index
for i in Index :
    print (NumList [i] )