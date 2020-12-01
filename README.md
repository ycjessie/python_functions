# Python Function Challenges

<br>

## Instructions

1. Fork and clone this repo
2. `cd` into the directory and open in `code`
3. Put your work in the `starter.py` file.
4. in the terminal, run `python starter.py` to run the file


<br>

## Objectives

Now it's time to practice some of these Python skillz. Below are four challenges meant to tie together all the concepts that we've learned so far. You may have solved similar problems using JavaScript. That's great! Use that knowledge to apply the same abstract concepts but update the syntax to make it work for Python.

<br>

## Challenges

1. Write a function named `sum_to()` that takes a number parameter `n` and returns the sum of the numbers from 1 to n. For example:

```python
sum_to(6)  # returns 21
sum_to(10) # returns 55
```

<br>

2. Write a function named `largest()` that takes a list parameter and returns the largest element in that list. You can assume the list contents are all *positive* numbers. For example:

```python
largest([10, 4, 2, 231, 91, 54])  # returns 231
largest([1,2,3,4,0])  # returns 4
```

<br>

3. Write a function named `occurances()` that takes two string parameters and counts the number of occurrances of the second string inside the first string. For example:

```python
occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'ee')  # returns 1
occurances('fleep floop', 'fe')  # returns 0
```

<br>

4. Write a function named `product()` that takes an *arbitrary* number of parameters, multiplies them all together, and returns the product. (HINT: Review your notes on `*args`).

<br>

5. DRY Up Some Code. Read the following Python code that violates the principle of *don't repeat yourself* (DRY).

```python
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
```

* Rewrite it to use FUNctions instead of repeating code
* Consider what your arguments and return values should be
* This one can be tricky, try working together with a classmate!
* Don't forget to commit your progress as you go along
* There can be multiple possible ways to solve this problem! But if you're stuck, some **hints** are provided below
* Try to open only one hint at a time!

#### For the purposes of this this assignment, do not use a list!

### (Spoiler Alert)

<details>
<summary>Hint 1</summary>
There is no need to re-write the "Awards Ceremonies" part of the code, because it's not repeated!
</details>

<details>
<summary>Hint 2</summary>
Start by writing a FUNction to ask for the distance that a person has run. e.g. `ask_for_distance`

What argument(s) does this FUNction need?

What should be the return value of this FUNction?
</details>

<details>
<summary>Hint 3</summary>
Try writing another FUNction to ask for the minutes that a person has run. e.g. `ask_for_minutes`

What argument(s) does this FUNction need? Just one or more than one?

What should be the return value of this FUNction?
</details>

<details>
<summary>Hint 4</summary>
Try writing another FUNction to compute the speed in terms of feet per second. e.g. `compute_speed`

What argument(s) does this FUNction need? Just one or more than one?

What should be the return value of this FUNction?
</details>

<details>
<summary>Hint 5</summary>
Try writing another FUNction that uses all of the previous 3 FUNctions that we wrote. e.g. `run`

This FUNction should ask for that particular runner's distance, ask for that particular runner's minutes, and then compute the speed.

What argument(s) does this FUNction need? Just one or more than one?

What should be the return value of this FUNction?
</details>

<details>
<summary>Hint 6</summary>
That's all I got for ya!!!!
</details>


<br>


# 6. (STRETCH) Challenge Yourself

_Exercise 6 is **optional** if you would like to challenge yourself. You are **not expected** to complete this part. Difficulty: Medium/Hard_

## Part 1

Write a FUNction called `is_even` that accepts a number as an argument and returns a boolean (true/false) indicating whether that number is even or not even (that is, odd).

**Hint**: use the `%` operator.

Be sure to try calling it with different numbers.

## Part 2

Let's write a FUNction `wrap_text` that wraps text in symbols of our choice.

For example:

```python
wrap_text('hello', '===')
```

should return:

```
===hello===
```

Now that this FUNction works, how can we use it (**without modifying the FUNction**) to generate the following string?

```
---===###new message###===---
```

**Important**: Your function `wrap_text` needs to **return** a value rather than **print** one.

**Hints**:

* You'll have to call the same FUNction multiple times
* Try breaking down the problem into smaller pieces that you know `wrap_text` can solve!
* This is a hard one, to challenge those who are a bit more advanced. It's OK if you don't get how to solve it right now. You can come back and solve it another day!

---

# All Done!

I bet you've had enough of FUNctions by now, go have some real fun!

![](https://media.giphy.com/media/xT0BKiK5sOCVdBUhiM/source.gif)


