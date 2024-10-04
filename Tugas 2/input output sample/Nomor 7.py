#input int of barrel 
gallons = int (input("How many gallons used?"))
#efisiensi alat 
efficiency = int (input ("The efficiency is (%): "))
#bcs 1 barrel equal 42 gallons
barrel= gallons/42
#the equivalent in BTU
equivalent = 58e5
#How to count the large of heat 
BTU = round (barrel*equivalent*efficiency/100,2)

print ("The large of heat is", BTU, "BTU")


