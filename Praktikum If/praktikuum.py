x1,y1 = map (int,input ("").split ())
xs,ys = map (int,input ("").split ())
xf,yf = map (int,input ("").split ())

distance = (xf-xs)**2 + (yf-ys)**2 
titik_awal = (xf-x1)**2 + (yf-y1)**2
if distance < titik_awal :
    print ("Yes")
else : 
    print ("No")