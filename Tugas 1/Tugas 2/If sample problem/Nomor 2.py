weight = float (input ("input your weight on kg : "))
height = float (input ("input your height on cm:"))
weight_lb = round (weight*2.20462, 2)
height_in = round (height*0.393701, 2)
BMI_Calculate = (703*weight_lb)/ (height_in**2)

if BMI_Calculate < 18.5 : 
    print ("your weight status is Underweight")
elif BMI_Calculate <= 24.9 : 
    print ("your weight status is Normal")
elif BMI_Calculate<= 29.9 :
    print ("your weight status is Overweight")
else : 
    print (" your weight status is Obese")