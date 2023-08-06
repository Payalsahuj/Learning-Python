# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"
def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    return sorted(word1) == sorted(word2)

word1 = "cinema"
word2 = "iceman"
result = is_anagram(word1, word2)
print(result)


# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


input_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(input_list)
print(sorted_list)


# 3. **Longest Common Prefix**: Given a list of strings, find the longest common prefix.
#     - *Input*: ["flower","flow","flight"]
#     - *Output*: "fl"
def longest_common_prefix(strs):
    if not strs:
        return ""

    strs.sort()

    prefix = ""
    for i in range(min(len(strs[0]), len(strs[-1]))):
        if strs[0][i] == strs[-1][i]:
            prefix += strs[0][i]
        else:
            break

    return prefix


input_list = ["flower", "flow", "flight"]
output = longest_common_prefix(input_list)
print(output) 


# 4. **String Permutations**: Write a Python function to calculate all permutations of a given string.
#     - *Input*: "abc"
#     - *Output*: "['abc', 'acb', 'bac', 'bca', 'cab', 'cba']"

def string_permutations(s):
    if len(s) <= 1:
        return [s]

    result = []
    for i in range(len(s)):
        fixed_char = s[i]
        remaining_chars = s[:i] + s[i + 1:]

        perms_of_remaining = string_permutations(remaining_chars)

        for perm in perms_of_remaining:
            result.append(fixed_char + perm)

    return result


input_str = "abc"
output = string_permutations(input_str)
print(output) 



# **Implement Queue using Stack**: Use Python's stack data structure to implement a queue.
#     - *Input*: enqueue(1), enqueue(2), dequeue(), enqueue(3), dequeue(), dequeue()
#     - *Output*: "1, None, 3, None, None"
class QueueUsingStack:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        if not self.dequeue_stack:
            return None

        return self.dequeue_stack.pop()


queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue()) 
queue.enqueue(3)
print(queue.dequeue()) 
print(queue.dequeue()) 
print(queue.dequeue())  

