num1=10
num2=14
num3=12

if(num1>=num2)&(num1>=num3):
    if(num2>=num3):
        secondlargest=num2
    else:
        secondlargest=num3
elif(num2>=num1)&(num2>=num3):
    if(num1>num3):
        secondlargest=num1
    else:
        secondlargest=num3
elif(num1>=num2):
    secondndlargest=num1
else:
    secondlargest=num2

print("The 2ndlargest ",secondlargest)