# %% [markdown]
# # preExperiment 4!
# rename the file name to 's' followed by your ID.

# %% [markdown]
# ### question 1
# 
# Open new code cell below this one and print the results of next expressions (each expression in his on line):
# 
#     1) 1+2
# 
#     2) 5*10
# 
#     3) 5*10+7
# 
#     4) 5*(10+7)
# 
#     5) 10**2
# 
#     6) 9**0.5
# 
#     7) 77%2
# 
#     8) 18//5

# %%
print(1+2)
print(5*10)
print(5*10+7)
print(5*(10+7))
print(10**2)
print(9**0.5)
print(77%2)
print(18//5)

# %% [markdown]
# ### question 2
# Open new code cell below this one and use at least 4 mathematecal opretors on any numerical valus you prefer to get 85.75 as a rasult and print it.

# %%
# Using 4 mathematical operators to achieve the result 85.75
result = (100-20) * 1.5 / 2 + 25.75
print(result)  # Output: 85.75

# %% [markdown]
# ### question 3
# 
# Use object names to keep better track of what's going on in your code!
# 
# Open new code cell below this one and assign to variables the numerical valus you use in question 2, and use them to get 85.75 and print is.
# 
# For example: 
#    
# instead:
# 
# <code>print(4\*5+3)</code>
# 
# write:
# 
# <code>a = 4</code>
# 
# <code>b = 5</code>
# 
# <code>c = 3</code>
# 
# <code>d = a*b+c</code>
# 
# <code>print(d)</code>
# 
# 

# %%
# Assigning the numerical values to variables
a = 100
b = 20
c = 1.5
d = 2
e = 25.75

# Using variables to calculate the result
f = (a - b) * c / d + e

# Printing the result
print(f)  # Output: 85.75

# %% [markdown]
# ### question 4
# assign to `a` an integer and to `b` a floa. Then write:
# ```python
# print(type(a))
# print(type(b))
# ```
# what did you get?

# %%
# Write your answer here

a = 1
b = 1.0 

print(type(a))
print(type(b))

# The result is:
# <class, 'int'>
# <class, 'float'>

# %% [markdown]
# ### question 5
# assign to `c` the number 7.548796521. Use the function `round()` and explain what the function did to the variable `c`. store the answer in the variable 'd'.
# 
# Print the type of the new variable 'd'.
# 
# for explain what `round()` did open new text cell below this one and write your explanation.
# 

# %%
# Write your answer here

c = 7.548796521
d = round (c)
print(d)

# The `round()` function in Python rounds a floating-point number to the nearest integer or to a specified number of decimal places.

# %% [markdown]
# ### question 6
# Assign to a the word 'hello'
# 
#    Type the next lines( each line in a new cell!!!!)
#     
#     a[0]
#     
#     a[1]
#     
#     a[2]
#     
#     a[3]
#     
#     a[4]
#     
#     a[5] --> Explain what happen in a text cell after the error!!
#     
#     a[-1] --> explain what happen.

# %%
# Assigning the word 'hello' to variable a
a = 'hello'

# %%
# Accessing the first character
a[0]  # Output: 'h'

# %%
# Accessing the second character
a[1]  # Output: 'e'

# %%
# Accessing the third character
a[2]  # Output: 'l'

# %%
# Accessing the fourth character
a[3]  # Output: 'l'

# %%
# Accessing the fifth character
a[4]  # Output: 'o'

# %%
# Accessing the sixth character (which doesn't exist)
a[5]  # This will raise an IndexError

# %%
a[-1]  # Output: '0'

# %% [markdown]
# ### question 7
# Now, after figuring how to call each letter, lets see if caught it.
# 
# Enter the word 'mississippi' to new variable and print all the 's' in the word by accessing their index on both sides!

# %%
# Assigning the word 'mississippi' to a variable
word = 'mississippi'

# Printing all the 's' in the word by accessing their indices on both sides
print(word[2])   # First 's' (index 2)
print(word[3])   # Second 's' (index 3)
print(word[5])   # Third 's' (index 5)
print(word[6])   # Fourth 's' (index 6)

# Accessing 's' from the end of the word using negative indexing
print(word[-5])  # Fourth 's' (index -5)
print(word[-6])  # Third 's' (index -6)
print(word[-8])  # Second 's' (index -8)
print(word[-9]) # First 's' (index -9)

# %% [markdown]
# ### question 8.1   
# assign to `a` the string **`it is a beatiful day`** using `""`. print `a`.

# %%
# Write your answer here
a = "it is a beautiful day"
print(a)

# %% [markdown]
# ### question 8.2
# 
# assign to `b` the string **`it's a beatiful day`** using `""`. print `b`.
# 
# If you are getting an error explain in new text cell why.

# %%
# Write your answer here
b = "it's a beautiful day"
print(b)

# %% [markdown]
# ### question 8.3
# 
# assign to `c` the sring **`it's a beatiful day`** using `''`. print `c`.
# 
# If you are getting an error explain in new text cell why.

# %%
# Write your answer here
c = 'it's a beautiful day'
print(c)

# An error occurred because the single quote (') inside the string is interpreted as the end of the string.

# %% [markdown]
# ### question 9.1
# print a sentence which tells how old are you.
# 'i am ? years old'

# %%
# Write your answer here
print('i am 24 years old')

# %% [markdown]
# ### question 9.2
# 
# Now store to variable `age` your age in type of int.
# 
# for example: `age = 16` → type(age) is integer.
# 
# try to print how old are you, and use format for insert age variable to the string.

# %%
# Write your answer here
age = 25
print(f"i am {age} years old")

# %% [markdown]
# ### question 10.1
# run the next code cell and in the followed cell write a code that print the next values:
# 
# 1. `sentence`
# 2. `mylist`
# 3. the type of `mylist`

# %%
sentence = 'Hi everybode and wellcome for today lecture'
mylist = sentence.split(' ')

# %%
# Write your answer here
print(sentence)
print(mylist)
print(type(mylist))

# %% [markdown]
# ### question 10.2
# The next code cell creating a list combined from several data types, run it.
# 
# Change the last value of `mylist` to a string value and then print `mylist` (by index and casting function)

# %%
mylist = [25, 'Hello', 22.5]
print(mylist)

# %%
# Write your answer here
mylist[-1] = str(mylist[-1])  # Accessing the last value by index (-1) and casting it to a string

# Printing the updated list
print(mylist)

# %% [markdown]
# ### question 11
# create the next list and use <code>.pop()</code> to eleminate the number 30 in this list. 
# 
# <code>mylist = [10,20,30,40,50,60]</code>
# 
# after using <code>.pop</code> print the list. 
# 

# %%
# Define the list
mylist = [10, 20, 30, 40, 50, 60]

# Use .pop() to remove the number 30
mylist.pop(2)  # 30 is at index 2

# Print the updated list
print(mylist)  # Output: [10, 20, 40, 50, 60]

# %% [markdown]
# ### question 12
# run the next cell and fix all the errors in it.

# %%
# the code need to print the last value of the my_newlist
sentence = 'Lecture 1 Lecture 2 Lecture 3 Lecture 4'
my_newlist = sentence.split(' ')
location = len(my_newlist) -1
lastvalue = my_newlist.pop(location)
print(lastvalue)

# %% [markdown]
# 
# ### question 13
# insert the next code <code>new_list = ['P','y','t','h','o','n']</code> to the cell below and use the next methods on new_list
# :
# 
#     1) .reverse()
#     2) .sort()
# print the objects you get and explain in the text cell about the methods.

# %%
# Creating the list
new_list = ['P', 'y', 't', 'h', 'o', 'n']

# Using the reverse method
new_list.reverse()
print("Reversed List:", new_list)

# Using the sort method
# Sorting the list elements in ascending alphabetical order
new_list.sort()
print("Sorted List:", new_list)

# %% [markdown]
# ### Write your explain here
# 
# 1. .reverse:  
# 2. .sort:

# %%
# .sort() - Sorting the list elements in ascending alphabetical order
# .reverse() - Reversing the order of the list elements

# %% [markdown]
# ### question 15
# insert the list - <code>[[1,2,3],[4,[5,6,7]],[[8,9,10],11,12]]</code> to new variable named <code>list_number</code>: 
# 
# print the sublist <code>[5,6,7]</code> by going to the location of the list_number: 

# %%
# Write your answer here
# Insert the list into the variable
list_number = [[1, 2, 3], [4, [5, 6, 7]], [[8, 9, 10], 11, 12]]

# Print the sublist [5, 6, 7]
print(list_number[1][1])  # Accessing the second element of the second sublist

# %% [markdown]
# # Practice using functions
# 
# In the following questions, **replace** the word 'pass' with your code in order for the function to perform its purpose.

# %% [markdown]
# ### question 16
# Define a function <code>MaxOfThree()</code> that takes three numbers as arguments and returns the largest of them (Use <code>if</code>, <code>elif</code> and <code>else</code>). For example, <code>MaxOfThree(1,  2,  3)</code> should return 3.

# %%
def MaxOfThree(a, b, c):
    if a >= b and a >= c:  # Check if 'a' is the largest
        return a
    elif b >= a and b >= c:  # Check if 'b' is the largest
        return b
    else:  # If neither 'a' nor 'b' is the largest, 'c' must be
        return c

# %%
print(MaxOfThree(1,  2,  3))

# %% [markdown]
# ### question 17
# Define a function <code>MySum()</code> and a function <code>MyMultiply()</code> that sums and multiplies (respectively) all the numbers in a list of numbers (Use <code>for</code>). For example, s <code>MySum([1, 2, 3, 4])</code> should return 10, and <code>MyMultiply([1, 2, 3, 4])</code> should return 24.

# %%
def MySum(inputList):
    pass

# %%
print(MySum([1, 2, 3, 4]))

# %%
def MyMultiply(inputList):
    pass

# %%
print(MyMultiply([1, 2, 3, 4]))

# %% [markdown]
# ### question 18
# Define a function <code>MyStars()</code> that takes a list of integers and prints a string of stars which has the length of a value of an integer to the screen. For example, <code>MyStars([3, 9, 7])</code> should print the following:
# 
# \*\*\*
# 
# \*\*\*\*\*\*\*\*\*
# 
# \*\*\*\*\*\*\*

# %%
def MyStars(inputList):
    pass

# %%
MyStars([3, 9, 7])


