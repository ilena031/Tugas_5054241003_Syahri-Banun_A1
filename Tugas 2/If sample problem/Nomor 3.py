def fun1 () : 
    z= (input ("Enter T for true or F for false : "))
    if z== "T": 
        return 1 
    else : 
        return 0 

def fun2 () :
    print ("fun2 excuted")
    return 1 

def main () : 
    print ("Testing &&")
    if fun1 () and fun2 () : 
        print ("Test of && complete")
    print ("Testing || ")
    if fun1 () or fun2 () :
        print ("Test of || complete")
main ()
   
