def DataUsage () :
    #User have to input datausage (n) on gbs 
    n = float (input ("input your datausage every month on GBs: "))
    #u get charge if u using the data usage within this interval 
    if n< 0 : 
        charge = "Invalid data usage"
    # 0.0<n<= 1.0 
    else : 
        if n<1.1 :
            charge = 250
    # 1.0 < n <= 2.0
        elif n< 2.1 : 
            charge = 500
    #2.0 < n <= 5.0 
        elif n<5.1 : 
           charge = 1000
    #5.0 < n <= 10.0
        elif n<10.1 : 
            charge = 1500
    #n>10.0
        elif n > 10.0 : 
            charge = 2000

    print ("your charges is $", charge)
DataUsage()