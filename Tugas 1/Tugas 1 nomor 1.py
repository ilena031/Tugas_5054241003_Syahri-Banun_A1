#variabel begining on odometer
begining = float(input ("Enter your begining odometer :"))
#variabel ending on odometer, float cs could incl comma
ending = float (input ("Enter your ending odometer :"))
#variabel cost per mile, float cs have a comma
cost = float (input("Cost per miles is : "))
#the distances of passanger
distances = round(ending-begining,1)
#final fare is distances times cost
fare = round(distances*cost, 2)

print ("You traveled a distance of", distances, "miles. At", cost, "per mile, your fare is $" ,fare)




