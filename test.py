user_input= int(input("Please enter the number you want to compare."))
if user_input>10:
print("This program will give you the sum of natural numbers from 1 to 10.")
sum=0
for i in range (1,11):
    sum=sum +i
print(f"The sum of natural numbers from 1 to 10 is {sum}")    