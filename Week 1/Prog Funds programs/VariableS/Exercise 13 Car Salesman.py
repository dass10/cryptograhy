# Author name: Shweta Das
# Date: 21 August 2021
# Quick Description: Car Salesman program 


carmodel = input("What is the car model:")
yearofthecar = input("What is the year of the car:")
basepriceofthecar = input("Please enter the base price of the car:")
basepriceofthecar1 = int(basepriceofthecar) 

 
tax = float(basepriceofthecar)*0.125

licensefee = 100
dealerfee = 500
destinationcharge = 300
#Here the base price of the Car value is an integer
totalcost = int(basepriceofthecar)+tax+licensefee+dealerfee+destinationcharge

#empty print also can be use to give an inline space
print("")
print("")
print("Total cost")
print("")
print(totalcost)

