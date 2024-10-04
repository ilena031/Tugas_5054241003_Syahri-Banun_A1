month = int(input ("Enter month (1-12) : ") )
day = int(input ("Enter day (1-31) : "))
year = int (input ("Enter the year : "))

#menghitung tahun kabisat, return 1 kalo kabisat, 0 kalo non kabisat
def leap_year(year) : 
    if (year%4 == 0 and year% 100 != 0 ) or (year%400 == 0 and year%100 == 0) : 
        return 1 
    else : 
        return 0 
    
#hitung hari berdasarkan bulan 
def days_count(month,day,year) : 
    #jumlah tanggal tiap bulan di tahun non kabisat 
    days_everymonth= [31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) == 1 : 
        days_everymonth[1] = 29
    #menghitung hari dalam setahun 
    dayintotal = (sum(days_everymonth[:month- 1])+day)
    hasil =  dayintotal
    return (hasil)

print (month,day,year, "is day", days_count(month,day,year))


