Total_Purchase = float (input ("How much the total of your purchase?"))
Student = str (input("Is the purchaser a student? (true or false)"))

if Student == "true" : 
    discounted = 20/100 * Total_Purchase
    Total_discounted = Total_Purchase-discounted
    sales_tax = discounted*(100-5)/100
    total = discounted+sales_tax
    print ("Total Purchases  $ "       , Total_Purchase )
    print ("Student's dicount (20%)"   , discounted )
    print ("Discounted total"          , Total_discounted )
    print ("Sales tax (5%)"            , sales_tax )
    print ("Total"                     , total)

else :
    Sales_tax = Total_Purchase*(100-5)/100
    Total = Total_Purchase-Sales_tax
    print ("Total Purchases         $ " , Total_Purchase)
    print ("Sales tax (5%)"            ,  Sales_tax )
    print ("Total"                     ,  Total)