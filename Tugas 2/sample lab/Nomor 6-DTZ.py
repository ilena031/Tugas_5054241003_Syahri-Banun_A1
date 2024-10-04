import datetime
#strptime berfungsi untuk merepresantasikan waktu dengan format tertentu
Ali_Time = datetime.datetime.strptime(input("Input Ali's Time (CH:CM:CS): "), ' %H:%M:%S')
Stream_Time = datetime.datetime.strptime(input("Streaming Time (HH:MM:SS): "), '%H:%M:%S')

#changes ali's time first, timedelta berfungsi untuk mengubah waktu 
Ali_Time -= datetime.timedelta(hours=5)
# Subtract Stream_Time from Ali_Time
Time_Difference = Stream_Time - Ali_Time 

if Time_Difference <= datetime.timedelta(hours=0, minutes=0, seconds=0):
    print("See you on the next Pear Event!")
else:
    print("Time difference:", Time_Difference)