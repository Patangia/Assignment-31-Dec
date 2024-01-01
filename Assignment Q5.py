'''
a=eval(input("Please enter your age = "))
print(a)

if(a>=18):
    print("Congratulation You are Elagible for Vote")
else:
    print("We are Sorry You are not Elagible for Vote")
'''

a=input("Year of Birth or Age = ")
if(a=="Year"):
    a=eval(input("Tell me your Birth Year = "))
    print(2023-a)
if(a=="Age"):
    a=eval(input("Tell me your Age = "))
if(a>=18):
    print("Congratulation You are Elagible for Vote")
else:
    print("We are Sorry You are not Elagible for Vote")

