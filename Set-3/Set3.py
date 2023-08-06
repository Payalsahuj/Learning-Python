# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."

people = [("John", 25), ("Jane", 30)]

for name, age in people:
    print(f"{name} is {age} years old.")


# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"
def add_name_age(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, new_age):
    if name in dictionary:
        dictionary[name] = new_age

def delete_name(dictionary, name):
    if name in dictionary:
        del dictionary[name]

people = {}

add_name_age(people, "John", 25)
print(people) 
update_age(people, "John", 26)
print(people) 
delete_name(people, "John")
print(people)  


# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"

def two_sum(nums, target):
    num_dict = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], index]
        num_dict[num] = index

    return None

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)


# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

def is_palindrome(word):
    cleaned_word = word.replace(" ", "").lower()
    reversed_word = cleaned_word[::-1]

    if cleaned_word == reversed_word:
        return True
    else:
        return False


input_word = "madam"
if is_palindrome(input_word):
    print(f"The word {input_word} is a palindrome.")
else:
    print(f"The word {input_word} is not a palindrome.")


# 1. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"

def selectionsort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j


        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


input_list = [64, 25, 12, 22, 11]
sorted_list = selectionsort(input_list)
print(sorted_list) 


# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"

from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue = Queue()

    def push(self, value):
    
        temp_queue = Queue()
        while not self.queue.empty():
            temp_queue.put(self.queue.get())

      
        self.queue.put(value)

       
        while not temp_queue.empty():
            self.queue.put(temp_queue.get())

    def pop(self):
        if self.queue.empty():
            return None
        return self.queue.get()


stack = StackUsingQueue()
stack.push(1)
stack.push(2)
print(stack.pop())
stack.push(3)
print(stack.pop()) 
print(stack.pop())  
print(stack.pop())  

# 1. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
#     - *Input*: None
#     - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=", ")
        elif num % 3 == 0:
            print("Fizz", end=", ")
        elif num % 5 == 0:
            print("Buzz", end=", ")
        else:
            print(num, end=", ")

fizzbuzz()




# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"

def count_words(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        # Count the number of words in the content
        word_count = len(content.split())

        with open(output_file, 'w') as file:
            file.write(f"Number of words: {word_count}")

        print(f"Number of words: {word_count}")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


input_file = "input.txt"
output_file = "output.txt"
count_words(input_file, output_file)

# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

num1 = 5
num2 = 0
result = divide_numbers(num1, num2)
print(result) 
