a=input("Hi Bro, Tell me your Name = ")
print(a)
b=eval(input("Howz the temperature = "))
print(b)
if(b>30):
    print("It's Hot")
elif(b>15 and b<=30):
    print("It's Modurate")
elif(b>0 and b<=15):
    print("It's Cold")
else:
    print("It's Freezing")