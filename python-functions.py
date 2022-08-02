# 1.
from math import prod


def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum
# print(sum_to(3))

# 2.
def largest(nums):
  largest = 0 
  for n in nums:
    if n > largest: 
      largest = n
  return largest

# print(largest([1, 2, 3, 4, 0]))

# 3.
def occurrences(string, substr):
  return string.count(substr)

# print(occurrences('I dont know I feel like time is passing by. Maybe I will never no. No','no'))

#4.
def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

# print(product(-12,4))