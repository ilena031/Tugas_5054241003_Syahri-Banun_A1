print ("(1) First Free Service")
print ("(2) Second Free Service")

num = int (input ("Enter the free service number >> "))
#for input miles 
k = float (input ("Enter number of Miles >> "))
if k < 1500 :
    print ("Vehicle in good condition")
elif num == 1 and k<= 3000 :
    print ("Vehicle must be serviced")
elif num == 2 and k<= 4500 : 
    print ("Vehicle must be serviced")
else : 
    print ("Erorr")