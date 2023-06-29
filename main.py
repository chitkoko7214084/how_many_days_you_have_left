
#This program will tell you how many days, week, and months you have left until 90 years old after you insert your age.
#Chit Ko Ko.


age = input("What is your current age? ")


age = int(age)


x = age * 365
result_1 =  32850 - x

y = age*52
result_2 = (4680-y)

z= age*12
result_3=(1080-z)



print (f"You have {result_1} days, {result_2} weeks, and {result_3} months left.")




