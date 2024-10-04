string0 = "Syahri Banun"
string1= "5054241003"
string2= "Sumatera Selatan"

print ("Nama saya adalah ", string0)
print ("NRP ", string1)
print ("Asal daerah ", string2)
print ("Inisial Saya " + string0[0]+ string0[7])
print ("Nama belakang saya " +string0[7:])
print ("Nama panggilan saya " + string0 [7:])
string3 = "Saya mahasiswa RKA"

string4= string3.replace ("mahasiswa RKA", "bukan mahasiswa RPL") 
print (string4)
print (string2[0:3]+ string2[4:]) #deleting character in asal 
print (f"Nama saya {string0}, dipanggil \"{string0[7:]}\"") #escape sequencing

string5 = "Nama saya {0}, NRP saya {1}, umur saya {2}, saya berasal dari {3}".format ("Syahri Banun", "5054241003", 17, "Sumatera Selatan")
print (string5) #py string formating 

#1 deleting 1 karakter di asal
#2 escape sequencing in py 
# py string formating (example 1,2,3,4)
