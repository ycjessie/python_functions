# 1. Write a function named sum_to() that takes a number parameter n and returns the sum of the numbers from 1 to n. For example:
def sum_to(num):
    sum=0
    for n in range(1,num+1):
        sum += n
    return sum
print(sum_to(10))


# user=int(input("Enter a number: "))
# sum_to=0
# for n in range(1,user+1):
#     sum_to+=n
# print("Sum is ", sum_to)



# 2. Write a function named largest() that takes a list parameter and returns the largest element in that list. You can assume the list contents are all positive numbers. For example:

# num=([10, 4, 2, 231, 91, 54])
# sort_num=sorted(num)
# print(sort_num[-1])
def largest(num):   
    sort_num=sorted(num)
    print(sort_num[-1])
# largest([10, 4, 2, 231, 91, 54])
largest([1,2,3,4,0])


# 3. Write a function named occurances() that takes two string parameters and counts the number of occurrances of the second string inside the first string. For example:
def occurances(string,sub):
    count=string.count(sub)
    print(count)
occurances('fleep floop', "e")
occurances('fleep floop', "p")
# string=('fleep floop', "fe")
# string1=string[0]
# substring=string[-1]
# count=string1.count(substring)
# print(string1)
# print(substring)
# print(count)




# 4. Write a function named product() that takes an arbitrary number of parameters, multiplies them all together, and returns the product. (HINT: Review your notes on *args).
#an arbitrary number of parameters:https://www.w3schools.com/python/python_functions.asp
#math.prod https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/
import math
def product(*args):
    return math.prod(args)
print(product(6,2,3,4))




# 5. DRY Up Some Code. Read the following Python code that violates the principle of don't repeat yourself (DRY).

def ask_for_distance(person):
    return float(input(f"How far did person {person} run (in feet)?"))
def ask_for_minutes(person,distance):
    return float(input(f'How many minutes did person {person} run take to run {distance} feet?'))

def compute_speed(distance,minute):
    return distance/(minute*60)

distance1 = ask_for_distance(1)
mins1 = ask_for_minutes(1,distance1)
distance2 = ask_for_distance(2)
mins2 = ask_for_minutes(2,distance2)
distance3 = ask_for_distance(3)
mins3 = ask_for_minutes(3,distance3)

speed1 = compute_speed(distance1,mins1)
speed2 = compute_speed(distance2,mins2)
speed3 = compute_speed(distance3,mins3)

# Award Ceremonies
if speed3 > speed2 and speed3 > speed1:
    print(f'Person 3 was the fastest at {speed3} f/s')
elif speed2 > speed3 and speed2 > speed1:
    print(f'Person 2 was the fastest at {speed2} f/s')
elif speed1 > speed3 and speed1 > speed2:
    print(f'Person 1 was the fastest at {speed1} f/s')
elif speed1 == speed2 and speed2 == speed3:
    print(f'Everyone tied at {speed1} m/s')

print('Well done everyone!')
<br>


# 6. (STRETCH) Challenge Yourself - Exercise 6 is optional if you would like to challenge yourself. You are not expected to complete this part. Difficulty: Medium/Hard

# Part 1 - Write a FUNction called is_even that accepts a number as an argument and returns a boolean (true/false) indicating whether that number is even or not even (that is, odd).
def is_Even(num):
    if(num%2==0):
        print(f"{num} is an even number")
    else:
        print(f"{num} is a odd number")
is_Even(33)

# Part 2 - Let's write a FUNction wrap_text that wraps text in symbols of our choice.
