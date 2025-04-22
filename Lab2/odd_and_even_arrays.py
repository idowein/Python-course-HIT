even_list=[]
odd_list=[]

num=int(input("Please enter a num"))

while num != -1:
    if num % 2 == 0:
        even_list. append(num)
    else:
        odd_list.append((num))
    num = int(input("Enter any num"))

print("Even list : {}".format(even_list))
print("Odd list : {} ".format(odd_list))