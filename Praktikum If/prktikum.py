U = int (input ())
K = int (input ())
M = int (input ())

DamageMinion = (M//2)*2*1 #Hp #dikali 2 karena AP yang diterima ucup ketika minion menyerang 
DamageKnight = (K//2)*5*5 #Hp #dikali 5 karena AP yang diterima ucup saat knight menyeraang yakni 5 
DamageRaja = 100*10 #Hp
TotalDamage = DamageMinion+DamageKnight+DamageRaja

sisaHp = U-TotalDamage

if sisaHp > 0 : 
    print ("Yeay Ucup Menang! Hp tersisa: ", sisaHp)
else : 
    print ("Yah! Ucup Meninggoy")