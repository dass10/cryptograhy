# Author name: Shweta Das
# Date: 22 August 2021
# Quick Description: More than one condition!Program



username = input("Enter username:")

password = input("Enter password:")

if username == "Arthur" and password == "victory":
                 print("McArthur: Welcome to flight simulater!:")

#use elif statement if wants to allow another set of username and password 
elif username == "Shweta" and password == "unitec":
                print("Shweta: Welcome to flight simulater!:")  
                


                

else:
    print("Wrong username or password")

