# Author name: Shweta Das
# Date: 22 August 2021
# Quick Description: Program to Calculate Grade of Student




final_mark = int(input("Enter Final Marks Obtained:"))

if final_mark > 50: 
    print("Error! invalid final mark")
elif final_mark >=40: 
    print("Students'Grade is A")
elif final_mark >= 35: 
    print("Students'Grade is B")
elif final_mark >= 30:
    print("Students'Grade is C")
elif final_mark < 30 and final_mark > 0:
    print("Students'Grade is D")
elif final_mark < 0:
	print("Error! invalid final mark")
