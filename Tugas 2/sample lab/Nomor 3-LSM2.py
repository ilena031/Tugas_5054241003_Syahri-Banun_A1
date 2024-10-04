def LSM () :
    N = int (input ("number's given (1-1000): "))
    C = int (input ("Who start fisrt? (1) for Lala and (2) for Lili : "))

    #if N = 1,2,5 the one who start is the winner 
    if N == 1 or 2 or 5 : 
        if C == 1 : 
            print ("Lala's the winner")
        else : 
            print ("Lili's the winner")

    #if N<6 and not 1,2,5. the second person's the winner 
    elif N<6 : 
        if C==1 : 
            print ("Lili's the winner")
        else : 
            print ("Lala's the winner")

    #if N>1000 and N<1 
    elif N<1 or N>1000 : 
        print ("Numbers error")

    #if N>=6 
    elif N>5 : 
        for i in range (N) : 
            return True 


LSM ()
            