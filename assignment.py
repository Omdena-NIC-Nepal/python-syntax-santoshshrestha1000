name = str("Santosh")
age = int (27)
print(f"My name is {name} and my age is {age}")
    #pass

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    pass
num1=15
num2=5
if num1>num2:
    print(f"{num1} is greater than {num2}")

#num1= int(input("Please enter the number you want to compare with number 10 : "))
num1=15
if num1>10:
    print("Given number is greater than 10")
elif num1<10:
    print("Given number is lesser than 10")
elif num1==10:
    print("Given number is equal to 10")
else:
    print("Given could not compare. Thanks")

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    pass
print("This program will give you the sum of natural numbers from 1 to 10.")
#
# n=int(input("Please enter the number that you want to calculate sum of numbers from 1 to n using a loop :  ")) 
sum=0
for i in range (1,11):
    sum=sum +i
print(f"The sum of natural numbers from 1 to 10 is {sum}")

print("This program will give you the sum of natural numbers from 1 to 10.")
sum=0
for i in range (1,11):
    sum=sum +i
print(f"The sum of natural numbers from 1 to 10 is {sum}")


def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    pass
numbers=[1,2,3,4,5]
print(numbers)
total=0
for i in numbers:
    total = total+i
print(f"The total of given numbers is {total}")
max_num= max(numbers)
print(f"The maximun number is the list is {max_num}")
min_num= min(numbers)
print(f"The minimun number in the list is {min_num}")
print(f"({total}, {max_num}, {min_num})")


def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    pass
students = {
        "John": 85,
        "Alice": 90,
        "Bob": 75,
        "Eve": 95
    }
more_than_80={name: val for name, val in students.items() if val>80}
print(more_than_80)


def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    pass
#def set_operations(list1, list2):
list1={"Apple", "Mango", "Orange", "Potato"}
list2={"Cauliflower", "Cabbage", "Radish", "Potato", "Orange"}
common_elem=list1.intersection(list2)
print(common_elem)



def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    pass
num_1=float(5.5)
num_2=float(15.5)

sum=num_1+num_2
difference=num_1-num_2
product=num_1*num_2
quotient=num_1/num_2

print(f"[sum: {sum}, difference: {difference}, product: {product}, quotient: {quotient} ")



def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    pass

age=18
citizen="new_zealand"

if age>=18 and citizen=="new_zealand":
    print("Woow, you are eligible to vote")
else:
    print("Oops, you are not eligible for vote.")

if age<=18 or citizen=="new_zealand":
    print("You are eligible for discount.")
else:
    print("Oops! you are not eligible for discount.")
#AND
a = True
b = False

result = a and b
print(result)  # Output: False

# Example with conditions
age = 27
is_active = True

# Both conditions must be true
can_apply = (age > 18) and is_active
print(can_apply)  # Output: True

#OR
a = True
b = False

result = a or b
print(result)  # Output: True

# Example with conditions
age = 16
has_permission = False

# At least one condition must be true
can_apply = (age > 18) or has_permission
print(can_apply)  # Output: False


#NOT
a = True

result = not a
print(result)  # Output: False

# Example with a condition
is_member = False

# Reverse the condition
can_enter = not is_member
print(can_enter)  # Output: True



def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    pass

def test_bitwise_ops():
    result = bitwise_ops(12, 10)
    assert result["and"] == 8
    assert result["or"] == 14
    assert result["xor"] == 6

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
a=int(12)
b=int(10)

#result a&b
   # print(result)

#result a|b

 #   print(result)