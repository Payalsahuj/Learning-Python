##print
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")

    print("")



# Problem **2: Display numbers from a list using loop**
# Write a program to display only those numbers from a list that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

num_list=[12, 75, 150, 180, 145, 525, 50]

for ele in num_list:
    if ele>500: break
    if ele>150: continue
    if ele%5==0: print(ele)


# Problem **3: Append new string in the middle of a given string**
# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.
s1 = "Ault"
s2 = "Kelly"
mid_index = len(s1) 
s3 = s1[:mid_index] + s2 + s1[mid_index:]

print(s3)



# Problem **4: Arrange string characters such that lowercase letters should come first**
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
string = "PyNaTive"
s1=""
s2=""
for ele in string:
    if ele.isupper(): 
        s1+=ele
    else: 
        s2+=ele

s3=s2+s1
print(s3)


# Problem **5: Concatenate two lists index-wise**
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result_list = []
min_len = min(len(list1), len(list2))
for i in range(min_len):
    result_list.append(list1[i] + list2[i])


result_list += list1[min_len:]
result_list += list2[min_len:]

print(result_list)



### Problem **6: Concatenate two lists in the following order**
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]


result_list = [x + y for x in list1 for y in list2]

print(result_list)


### Problem **7: Iterate both lists simultaneously**
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, reversed(list2)):
    print(x, y)


### Problem **8: Initialize dictionary with default values**
# In Python, we can initialize the keys with the same values.
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

employee_data = {employee: defaults.copy() for employee in employees}

print(employee_data)



### Problem **9: Create a dictionary by extracting the keys from a given dictionary**
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}


keys = ["name", "salary"]

new_dict = {key: sample_dict[key] for key in keys}

print(new_dict)





# Problem 10: Modify the tuple
# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222
nested_tuple = ((11, [22, 33]), 44, 55)
nested_list = list(nested_tuple[0])
nested_list[0] = 222
modified_tuple = (tuple(nested_list),) + nested_tuple[1:]

print(modified_tuple)
