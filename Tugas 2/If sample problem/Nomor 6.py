#input the coordinate
x,y = map (float, input ("Input the value of x,y : ") .split ())
#classfied quadran
if x> 0 and y>0 : 
    print ( "(", x,y , " ) is in quadrant I") 
elif x<0 and y>0 : 
    print ( "(", x,y , " ) is in quadrant II")
elif x<0 and y<0 : 
    print ( "(", x,y , " ) is in quadrant III")
elif x>0 and y<0 : 
    print ( "(", x,y , " ) is in quadrant IV")
else : 
    print ( "(", x,y , " ) do not lie on quadrant")

#classified the axis 
if x==0 and y!= 0: 
    print ( "(", x,y , " ) is on the y-axis")
elif y== 0  and x!=0 : 
    print ( "(", x,y , " ) is on the x-axis")
