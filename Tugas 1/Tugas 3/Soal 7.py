#user input
cmd, K = map(int, input("").split())
shifted_text = []

while True : #looping line 
    text = input () #user input text
    if text == 'END' :
        break 
    
    if cmd == 1 : #encrypted 
        for char in text : #iteration each character on the text 
            if 'A' <= char <= 'Z' : #upeercase letter
                another_char = chr(((ord(char)- ord ('A')+ K)%26) + ord ('A')) #shifting with ASCII Value to a new char 
            elif 'a' <=char <= 'z' : #lowecase letter 
                 another_char = chr(((ord(char)- ord ('a')+ K)%26) + ord ('a')) #shifting with ASCII Value to a new char 
            else : 
                another_char = char #other character still with that 
            shifted_text.append (another_char)
    elif cmd==2 : #decrypted
        for char in text : 
            if 'A' <= char <= 'Z' : #upeercase letter
                another_char = chr(((ord(char)- ord ('A')- K)%26) + ord ('A')) #shifting with ASCII Value to a new char 
            elif 'a' <=char <= 'z' : #lowecase letter 
                another_char = chr(((ord(char)- ord ('a')- K)%26) + ord ('a')) #shifting with ASCII Value to a new char 
            else : 
                another_char = char #other character still with that 
            shifted_text.append (another_char)
    else : 
        print ("Error code")

    print (''.join (shifted_text))