# %%
def myDictConst(myVal, myKey):
    # Ensure both lists are of equal length
    if len(myVal) != len(myKey):
        raise ValueError("Both lists must have the same length.")
    
    # Create the dictionary using zip
    my_dict = dict(zip(myKey, myVal))
    
    return my_dict

# %%
# Example usage
myVal = [1, 2, 3, 'a']
myKey = ['b', 'c', 'd', 12.3]

result = myDictConst(myVal, myKey)
print(result)

# %%
def countMyStrings(myStr):
    # Normalize the string to lowercase and split into words
    words = myStr.lower().split()
    print(f"Splitted words : {words}")
    
    # Create a dictionary to count word occurrences
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

# %%
# Example usage
myStr = 'Hello Hello We Do Hi no No no we Donot Hey HE he hey'
myDict = countMyStrings(myStr)
print(myDict)


