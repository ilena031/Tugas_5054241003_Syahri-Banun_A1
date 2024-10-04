M = int (input ("total cars in front of you : "))
N = int (input ("total cars behind of you : "))
T = int (input ("the time : "))
#x melambangkan mobil kita
x = 1 
#traffic light 
redlight = 20 #second 
yellowlight = 5 #second 
greenlight = 60 #second 
cycle1 = (redlight+yellowlight+greenlight)
#waktu dibagi putaran traffic light 
car_round = T//cycle1
#waktu yang tersisa dari putaran tersebut 
remaining_time = ((T/cycle1)-car_round)*cycle1
#sisa waktu tersebut dibagi dengan putaran waktu selanjutnya (red n yellow light) untuk melambangkan mobil yang lewat setelah putaran 1
car_round2 = remaining_time//(yellowlight+redlight)

#hitung berapa mobil yang mungkin sudah melewati traffic light dalam putaran
car_passed = ((greenlight/5)*car_round)
#sisa mobil ketika mobil di putaran pertama dan sisa putaran lewat, ditambh dengan jumlah mobil kita
remaining_car = (M + N  - car_passed-car_round2+x)

if remaining_car == 0 : print ("YES!")
else : print ("NO!")

#print jumlah mobl yang tersisa 
print (remaining_car)