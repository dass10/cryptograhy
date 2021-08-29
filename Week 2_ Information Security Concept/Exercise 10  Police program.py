# Author name: Shweta Das
# Date: 22 August 2021
# Quick Description: Police program

print("Assuming the speed limit is 100 km/h")
speed = int(input("What was the speed detected:	"))

overunder = speed - 100

if (speed <=10):
    print("It'is speed less than 10km/h over the limit. The driver should be fined $30")

elif (speed >=10):
    print("It's 11 km/h over the limit. The driver should be fined $80")
    
elif (speed >=15):
    print("It's 16 km/h over the limit.The driver should be fined $120")
    
elif (speed >=20):
    print("It's 21 km/h over the limit.The driver should be fined $170")





