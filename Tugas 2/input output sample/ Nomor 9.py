#lenght and weith in yard
YardLenght = float (input("Input your yard lenght : "))
YardWidht = float (input("Input your yard widht : "))
HouseLenght = float (input ("Input your house lenght : "))
HouseWidht = float (input (" Input your house widht : "))

#luas sisa (luas taman-luas rumah)
RemainingArea = ((YardLenght*YardWidht)-(HouseLenght*HouseWidht))*9
#time required for cut the grasss (remainingarea/rate on feet)
Rate = input ("input ur rate on feet : ")
#to count time required
Time = round (RemainingArea/Rate,4)

print ("Time required to cut the grass with an area of",RemainingArea, "feet square is", Time, "second")

