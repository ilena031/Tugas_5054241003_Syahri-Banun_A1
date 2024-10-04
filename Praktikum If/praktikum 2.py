X,Y = map (int,input ("").split ())
x,y = map (int, input ("").split ())
M = int (input (""))
if (x==0 and y==0) or (x==0 and y==Y) or (x==X and y==0) or (x==X and y==Y) :
    space = 3 
elif (x== 0 or y==0 or x==X or y == Y) :
    space = 5 
else : 
    space = 8 

if M==1 : 
    mx,my = map (int,input ("").split())
elif M == 2 : 
    mx,my = map (int,input ("").split())
    mx2,my2 = map (int,input ("").split())
elif M == 3 : 
    mx,my = map (int,input ("").split())
    mx3,my3 = map (int,input ("").split())
    mx2,my2 = map (int,input ("").split())
    if (x+1 == mx or x-1 == mx) or (y+1 == my or y-1 == my) :
        space -= 1 
    if (x+1 == mx2 or x-1 == mx2) or (y+1 == my2 or y-1 == my2) :
        space -= 1 
    if (x+1 == mx3 or x-1 == mx3) or (y+1 == my3 or y-1 == my3) :
        space -= 1 
elif M==4 : 
    mx,my = map (int,input ("").split())
    mx4,my4 = map (int,input ("").split())
    mx3,my3 = map (int,input ("").split())
    mx2,my2 = map (int,input ("").split())
    if (x+1 == mx or x-1 == mx) or (y+1 == my or y-1 == my) :
        space -= 1 
    if (x+1 == mx2 or x-1 == mx2) or (y+1 == my2 or y-1 == my2) :
        space -= 1 
    if (x+1 == mx3 or x-1 == mx3) or (y+1 == my3 or y-1 == my3) :
        space -= 1 
    if (x+1 == mx4 or x-1 == mx4) or (y+1 == my4 or y-1 == my4) :
        space -= 1 
elif M==5 : 
    mx,my = map (int,input ("").split())
    mx5,my5 = map (int,input ("").split())
    mx4,my4 = map (int,input ("").split())
    mx3,my3 = map (int,input ("").split())
    mx2,my2 = map (int,input ("").split())
    if (x+1 == mx or x-1 == mx) or (y+1 == my or y-1 == my) :
        space -= 1 
    if (x+1 == mx2 or x-1 == mx2) or (y+1 == my2 or y-1 == my2) :
        space -= 1 
    if (x+1 == mx3 or x-1 == mx3) or (y+1 == my3 or y-1 == my3) :
        space -= 1 
    if (x+1 == mx4 or x-1 == mx4) or (y+1 == my4 or y-1 == my4) :
        space -= 1 
    if (x+1 == mx5 or x-1 == mx5) or (y+1 == my5 or y-1 == my5) :
        space -=1 
elif M ==6 : 
    mx,my = map (int,input ("").split())
    mx6,my6 = map (int,input ("").split())
    mx5,my5 = map (int,input ("").split())
    mx4,my4 = map (int,input ("").split())
    mx3,my3 = map (int,input ("").split())
    mx2,my2 = map (int,input ("").split())
    if (x+1 == mx or x-1 == mx) or (y+1 == my or y-1 == my) :
        space -= 1 
    if (x+1 == mx2 or x-1 == mx2) or (y+1 == my2 or y-1 == my2) :
        space -= 1 
    if (x+1 == mx3 or x-1 == mx3) or (y+1 == my3 or y-1 == my3) :
        space -= 1 
    if (x+1 == mx4 or x-1 == mx4) or (y+1 == my4 or y-1 == my4) :
        space -= 1 
    if (x+1 == mx5 or x-1 == mx5) or (y+1 == my5 or y-1 == my5) :
        space-=1
    if (x+1 == mx6 or x-1 == mx6) or (y+1 == my6 or y-1 == my6) :
        space -=1 
elif M ==7 : 
    mx,my = map (int,input ("").split())
    mx7,my7 = map (int,input ("").split())
    mx6,my6 = map (int,input ("").split())
    mx5,my5 = map (int,input ("").split())
    mx4,my4 = map (int,input ("").split())
    mx3,my3 = map (int,input ("").split())
    mx2,my2 = map (int,input ("").split())
    if (x+1 == mx or x-1 == mx) or (y+1 == my or y-1 == my) :
        space -= 1 
    if (x+1 == mx2 or x-1 == mx2) or (y+1 == my2 or y-1 == my2) :
        space -= 1 
    if (x+1 == mx3 or x-1 == mx3) or (y+1 == my3 or y-1 == my3) :
        space -= 1 
    if (x+1 == mx4 or x-1 == mx4) or (y+1 == my4 or y-1 == my4) :
        space -= 1 
    if (x+1 == mx5 or x-1 == mx5) or (y+1 == my5 or y-1 == my5) :
        space-=1
    if (x+1 == mx6 or x-1 == mx6) or (y+1 == my6 or y-1 == my6) :
        space -=1 
    if (x+1 == mx7 or x-1 == mx7) or (y+1 == my7 or y-1 == my7) :
        space -=1 
elif M == 8 : 
    mx,my = map (int,input ("").split())
    mx8,my8 = map (int,input ("").split())
    mx7,my7 = map (int,input ("").split())
    mx6,my6 = map (int,input ("").split())
    mx5,my5 = map (int,input ("").split())
    mx4,my4 = map (int,input ("").split())
    mx3,my3 = map (int,input ("").split())
    mx2,my2 = map (int,input ("").split())
    if (x+1 == mx or x-1 == mx) or (y+1 == my or y-1 == my) :
        space -= 1 
    if (x+1 == mx2 or x-1 == mx2) or (y+1 == my2 or y-1 == my2) :
        space -= 1 
    if (x+1 == mx3 or x-1 == mx3) or (y+1 == my3 or y-1 == my3) :
        space -= 1 
    if (x+1 == mx4 or x-1 == mx4) or (y+1 == my4 or y-1 == my4) :
        space -= 1 
    if (x+1 == mx5 or x-1 == mx5) or (y+1 == my5 or y-1 == my5) :
        space-=1
    if (x+1 == mx6 or x-1 == mx6) or (y+1 == my6 or y-1 == my6) :
        space -=1 
    if (x+1 == mx7 or x-1 == mx7) or (y+1 == my7 or y-1 == my7) :
        space -=1 
    if (x+1 == mx8 or x-1 == mx8) or (y+1 == my8 or y-1 == my8) :
        space -=1
else :
    space = 0 

if space > 0 : 
    print ("Senshi makan hari ini!")
else : 
    print ("Senshi makannya besok aja deh.")