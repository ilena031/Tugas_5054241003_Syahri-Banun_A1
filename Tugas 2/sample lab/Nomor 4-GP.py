#B is max distance is n 
n = int (input ("maximum distance is : "))
#input the distances of one pillar to other 
A_to_Bee, Bee_to_C, C_to_D, D_to_E = map (int,input ("Disntances of pillar one to other is (input 4 number): ").split (','))

if n <= A_to_Bee and Bee_to_C and C_to_D and D_to_E : print ("YES HE CAN")
else : print ("NO HE CAN'T")