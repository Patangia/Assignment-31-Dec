Maths=eval(input(" Enter the Student Maths Number = "))
Physics=eval(input(" Enter the Student Physic Number = "))
English=eval(input(" Enter the Student English Number = "))
Total_Marks=Maths+Physics+English
Percentage=(Total_Marks/300)*100
print(Percentage)

if(Percentage>100):
    print('It is incorrected Percentage')
elif(Percentage<=100 and Percentage>=90):
    print('A')
elif(Percentage<90 and Percentage>=80):
    print('B')
elif(Percentage<80 and Percentage>=70):
    print('C')
elif(Percentage<70 and Percentage>=60):
    print('D')
else:
    print('F')