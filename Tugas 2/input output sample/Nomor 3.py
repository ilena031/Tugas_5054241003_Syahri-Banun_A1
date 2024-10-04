#to enter the time 
timehour = int (input ("how long its started? (in hour) "))
timeminute = int (input ("how long its satarted? (in minute)"))/60
time= timehour+timeminute
#to count the temprature
ExactTemp = round(((4*time**2)/(time+2))-20,2)
print ("Your temprature is", ExactTemp, "°C")


