#The quantity of volume 
Quantity = int (input ("Volume to be infused (mL)"))

Time = int (input ("How long should be infused? (in minute)"))
#To count the rate of infuse
Rate = round ((Quantity/Time)*60, 4)

print ("The VBTI : ", Quantity, "mL")

print ("Rate :", Rate, "mL/hour")

