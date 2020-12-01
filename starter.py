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





# 3. Write a function named occurances() that takes two string parameters and counts the number of occurrances of the second string inside the first string. For example:





# 4. Write a function named product() that takes an arbitrary number of parameters, multiplies them all together, and returns the product. (HINT: Review your notes on *args).





# 5. DRY Up Some Code. Read the following Python code that violates the principle of don't repeat yourself (DRY).

print('How far did person 1 run (in feet)?')
distance1 = float(input())
print(f'How many minutes did person 1 run take to run {distance1} feet?')
mins1 = float(input())

print('How far did person 2 run (in feet)?')
distance2 = float(input())
print(f'How many minutes did person 2 run take to run {distance2} feet?')
mins2 = float(input())

print('How far did person 3 run (in feet)?')
distance3 = float(input())
print(f'How many minutes did person 3 run take to run {distance3} feet?')
mins3 = float(input())

secs1 = mins1 * 60
speed1 = distance1/secs1

secs2 = mins2 * 60
speed2 = distance2/secs2

secs3 = mins3 * 60
speed3 = distance3/secs3

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


# Part 2 - Let's write a FUNction wrap_text that wraps text in symbols of our choice.
