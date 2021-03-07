# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(x) that takes a string and returns
# the most common multiple of three in the string.
def count_threes(x):
  dictCount = {}
  for i in x:
    val = int(i)
    if(val % 3 == 0 and val != 0):
      if(i in dictCount):
        dictCount[i] += 1
      else:
        dictCount[i] = 1
  return int(max(dictCount, key=dictCount.get))

# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns a list of the characters that have the longest consecutive repeat.
# if there is a tie, it should return a list of characters
def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE
  numRepeats = 0
  longestRepeat = 0
  longestChar = ''
  lastChar = ''
  dictCount = {}
  for i in s:
    if(not i in dictCount):
      dictCount[i] = 0
    if(i == lastChar):
      numRepeats+=1
    else:
      if(numRepeats > dictCount[i]):
        dictCount[lastChar] = numRepeats
      numRepeats = 0
    lastChar = i
  if(numRepeats > dictCount[s[-1:][0]]):
    dictCount[s[-1:][0]] = numRepeats
  v = max(dictCount.values())
  re = []
  for i in dictCount.keys():
    if(dictCount[i] == v):
      re.append(i)
  return re


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE
  return s.lower().replace(" ", "")[::-1] == s.lower().replace(" ", "")
