# %% [markdown]
# # Experiment 5
# 
# **Topics of Experiment 5**
# 
# *   Using `for` loop in Python.
# *   Using `if elif else` in Python.
# *   Function and Methods.
# *   numpy library.
# 

# %%
Student = "Ido Weinstock"    # Student Name
ID = "211677083"         # ID
print(Student, ID)

# %% [markdown]
# ### Exercise 1 - 35 points
# 
# Create a function called `ExtractNonVowelStartingWords`.
# 
# This function should take a single string as its input and return a list containing only the words that **don't start** with a vowel (A, E, I, O, U). The function should be case-insensitive, meaning it should recognize vowels whether they are in uppercase or lowercase.
# 
# You are allowed to use the `.lower()` method if necessary (for more information, you can use `help(str.lower)`).
# 
# **Example 1:**
# 
# ```python
# sampleString = "I'm in a hurry because my bus isn't coming, so I have to find another way to get there."
# resultList = ExtractNonVowelStartingWords(sampleString)
# ```
# resultList → ['hurry', 'because', 'my', 'bus', 'coming', 'so', 'have', 'to', 'find', 'way', 'to', 'get', 'there.']
# 
# **Example 2:**
# 
# ```python
# sampleString = "Every action has an equal and opposite reaction."
# resultList = ExtractNonVowelStartingWords(sampleString)
# ```
# resultList → ['has', 'reaction.']

# %%
# answer exe 1 here!
def ExtractNonVowelStartingWords(strong):
    # Define a tuple containing all vowel characters (lowercase) for comparison
    vowels = ('a', 'e', 'i', 'o', 'u')
    # Split the input string into a list of words
    words = strong.split()
    # Initialize an empty list to store the result
    result = []
    # Iterate through each word in the list of words
    for word in words:
        # Check that the word is not empty and its first character (case-insensitive) is not a vowel
        if len(word) > 0 and word[0].lower() not in vowels:
            # If the word does not start with a vowel, add it to the result list
            result.append(word)
    # Return the list of words that do not start with a vowel
    return result


# %%
print(ExtractNonVowelStartingWords("I'm in a hurry because my bus isn't coming, so I have to find another way to get there."))
print(ExtractNonVowelStartingWords("Every action has an equal and opposite reaction."))

# %% [markdown]
# ### Exercise 2 - 35 points
# 
# Define a function named `countWordsNotStartingWithChars`.
# 
# The function should take two inputs:
# 1. A string composed of words.
# 2. A set of characters (string) to filter out words that start with any of them.
# 
# The function should return a dictionary where each key is a word that **doesn't start** with any of the given characters, and each value is the number of occurrences of that word. The function should be case-insensitive.
# 
# **Example:**
# 
# ```python
# myStr = 'Hello Hello We DO He no No no we'
# chars = 'Hn'
# stringHist = countWordsNotStartingWithChars(myStr, chars)
# ```
# stringHist → {'we': 2, 'do': 1}. **(The order of the words/keys does not matter)**
# 
# **Another Example:**
# 
# ```python
# myStr = 'Apple Banana Cherry Apple apricot banana'
# chars = 'AB'
# stringHist = countWordsNotStartingWithChars(myStr, chars)
# ```
# stringHist → {'cherry': 1}. **(The order of the words/keys does not matter)**

# %%
# answer exe 2 here!

def countWordsNotStartingWithChars(line, chars):
    # Convert the set of characters to lower-case for case-insensitive comparison
    chars = chars.lower()
    # Split the input string into individual words
    words = line.split()
    # Create an empty dictionary to store the results
    result = {}
    # Loop through each word in the list
    for word in words:
        # Convert the word to lower-case for case-insensitive comparison and counting
        word_lower = word.lower()
        # Check if the first character is not in the chars set
        if word_lower[0] not in chars:
            # If the word is already in the result dictionary, increment its count
            if word_lower in result:
                result[word_lower] += 1
            # Otherwise, add the word to the dictionary with count 1
            else:
                result[word_lower] = 1
    # Return the final dictionary with word counts
    return result

# %%
print(countWordsNotStartingWithChars('Apple Banana Cherry Apple apricot banana', 'AB'))

# %% [markdown]
# ### Exc 3 - 30 points
# 
# Define a function named `PlusMat`.
# The function input is two parameters.
# 
# 1.   `ms` – even number. represents the size of the matrix.
# 2.   `width_half` – natural number. Represents the thickness of the strips of the ones, the thickness of the entire strip is **twice**
# The `width_half`. the parameter has a default value of 1.
# 
# the function returns a matrix that is an ndarray array of dtype int.
# The plus is located exactly in the middle of the matrix.
# 
# Note: If the "ms" value is not an even number then the function should return None.
# 
# **example 1:**
# 
# ```pyton
# plus_1 = PlusMat(4)
# print(plus_1)
# 
# [[0 1 1 0]
#  [1 1 1 1]
#  [1 1 1 1]
#  [0 1 1 0]]
# ```
# 
# **example 2:**
# 
# ```pyton
# plus_2 = PlusMat(8, 2)
# print(plus_2)
# 
# [[0 0 1 1 1 1 0 0]
#  [0 0 1 1 1 1 0 0]
#  [1 1 1 1 1 1 1 1]
#  [1 1 1 1 1 1 1 1]
#  [1 1 1 1 1 1 1 1]
#  [1 1 1 1 1 1 1 1]
#  [0 0 1 1 1 1 0 0]
#  [0 0 1 1 1 1 0 0]]
# ```

# %%
# answer exe 3 here!
import numpy as np
def PlusMat(ms, width_half=1):

    # Check if ms is even
    if ms % 2 != 0:
        return None
    
    # Create a zero matrix of the given size
    mat = np.zeros((ms, ms), dtype=int)
    
    # Determine the center and thickness bounds
    start = ms//2 - width_half # integer (floor) division
    end = ms//2 + width_half    
    
    # Fill the central horizontal and vertical strips with ones
    mat[start:end, :] = 1       # horizontal strip. the ',' (coma) makes the command to select rows and all columns
    mat[:, start:end] = 1       # vertical strip. the ',' (coma) makes the command to select columns and all rows
    
    return mat

# %%
plus_1 = PlusMat(4)
print(plus_1)

plus_2 = PlusMat(8, 2)
print(plus_2)


