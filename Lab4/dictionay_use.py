# first option to use dictionary (efficient way)
def count_letter1(text):
    letter_count ={}
    for current_char in text:
        letter_count[current_char] = letter_count.get(current_char, 0)+1
    return letter_count

# second way to use dictionary (less efficient)
def count_letter2(txt):
    letter_count = {}
    for current_char in txt:
        if current_char not in letter_count:
            letter_count[current_char] = 1
        else: 
            letter_count[current_char]+=1
    return letter_count

example = count_letter1('mako')
print(example)

example2 = count_letter2('mako')
print(example2)


