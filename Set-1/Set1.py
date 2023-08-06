# Numbers: int, float, complex
# Strings: str
# Booleans: True and False
# Lists: list
# Tuples: tuple
# Dictionaries: dict
# Sets: set
# if, elif, else for conditional branching.
# for and while for loops.

# Write a Python program that prints "Hello, World!" to the console.
print("Hello world")


# Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.

integervar = 48
print(type(integervar))


floatvar = 5.6
print(type(floatvar))


stringvar = "Hello, World!"
print(type(stringvar))


booleanvar = True
print(type(booleanvar))


listvar = [1, 5, 3, 4, 5]
print(type(listvar))


tuplevar = (6, 0, 8, 9, 10)
print(type(tuplevar))


dictionaryvar = {"name": "payal", "age": 29, "city": "Raipur"}
print(type(dictionaryvar))


setvar = {1, 2, 3, 4, 5}
print(type(setvar))



# Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
numbers_list = list(range(1, 11))
print( numbers_list)

numberadd = 13
numbers_list.append(numberadd)
print(numbers_list)
numberremove=3
numbers_list.remove(numberremove)
print(numbers_list)

numbers_list.sort()
print(numbers_list)
numbers_list.sort(reverse=True)
print(numbers_list)



#Write a Python program that calculates and prints the sum and average of a list of numbers.

numberslist = [10, 20, 30, 40]
average=sum(numberslist) / len(numberslist)
sum=sum(numberslist)
print(sum,average)


#Write a Python function that takes a string and returns the string in reverse order.
def reversestring(inputstring):
    return inputstring[::-1]


string = "Hello"
revstring = reversestring(string)
print(revstring)



#Write a Python program that counts the number of vowels in a given string.

str = input("Enter a string:")
vowels="aeiouAEIOU"
count=0

for char in str:
  if char in vowels:
     count += 1

print("Number of vowels in the string:", count)

# Write a Python function that checks whether a given number is a prime number.
def isPrime(num):
   if num<=1:
      return False
   for  i in range(2,int(num**0.5+1)):
      if num%i==0:
       return False
      return True
print(isPrime(9))


#Write a Python function that calculates the factorial of a number.

def factorial(num):
   if num==0 or num==1:
      return 1
   ans=1
   for i in range(2, num+1):
    ans*=i
   return ans
   
print(factorial(5))


#Write a Python function that generates the first n numbers in the Fibonacci sequence.

def fibonacci(n):
   if n==0:
      return []
   elif n==1:
      return [0]
   
   fibo=[0,1]

   while len(fibo)<n:
      nex=fibo[-1]+fibo[-2]
      fibo.append(nex)

   return fibo
   
print(fibonacci(10))

#Use list comprehension to create a list of the squares of the numbers from 1 to 10.

square=[x**2 for x in range(1,11)]
print(square)