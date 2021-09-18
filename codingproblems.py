import math
import os
import random
import re
import sys

#Sales by Match
#https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(n, ar):
    
    colorFound = []
    pairs = 0

    for color in ar:
        if color in colorFound:
            colorFound.remove(color)
            pairs += 1
        else:
            colorFound.append(color)

    return pairs

# Time complexity O(n) (We have to iterate through each value of "ar"), Space Complexity O(n) (Worst case is we have an "ar" consisting of no pairs -
#  our colorsFound List would be the size of ar).

#-------------------------------------------------------------------------------------------------------------------

# Jumping on Clouds
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def jumpingOnClouds(c):
    
    i = 0
    cSize = len(c) - 1
    moves = 0
    
    while i < cSize:
        
        # Have to check if we're at least one index away from completion or else we'll throw an IndexError, but anytime we're there
        #  we can assume we only need to move a single space before completion.
        if i == (cSize - 1):
            moves += 1
            i += 1
        elif c[i + 2] == 0:
            i = i + 2
            moves += 1
        else:
            i = i + 1;
            moves += 1
                   
    return moves

# Time complexity is somewhere under 0(n), but this problem doesn't seem to have a big emphasis on optimization. Space complexity is constant.

#-------------------------------------------------------------------------------------------------------------------------------------------------

#Counting Valleys
#https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


def countingValleys(steps, path):
    
    height = 0
    lastStep = ""
    valleysTraversed = 0

    #Count each step and adjust our height accordingly

    for step in path:
        if step == "D":
            height -= 1
        else:
            height += 1
        lastStep = step
        
        #If we return to Sea Level AND our last step was up, then we always come out of a valley.

        if height == 0 and lastStep == "U":
            valleysTraversed += 1
    
    return valleysTraversed

#Time complexity is O(n) which is just counting every step. Unsure if I can optimize it any further, since we have to keep count relative to our starting point.
#Space complexity is constant, since we're only keeping track of three variables.

#----------------------------------------------------------------------------------------------------------------------------------

#Left Rotation
#https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def rotLeft(a, d):
    
    newArr = a.copy()
    rotationPointer = len(a) - d
    
    for value in a:
        if rotationPointer >= len(a):
            rotationPointer = 0
        
        newArr[rotationPointer] = value
        rotationPointer += 1

    return newArr

#--------------------------------------------------------------------------------------------------------------------------------------

# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

def lengthOfLongestSubstring(s):
    currStr = ["", 0]
    bestStr = ""
    i = 0
    while i < len(s):
        if s[i] not in currStr:
            currStr[0] = currStr[0] + s[i]
            if len(currStr[0]) > len(bestStr):
                bestStr = currStr[0]
            i += 1
        else:
            currStr = ["", ]
            currStr = currStr + s[i]
        i += 1
        
    return len(bestStr)

#--------------------------------------------------------------------------------------------------------------------------------------

def ratioOfNegatives(arr):
    neg = 0
    pos = 0
    zer = 0

    for int in arr:
        if int > 0:
            pos += 1
        elif int == 0:
            zer += 1
        else:
            neg += 1
    
    print("{:.5f}".format(neg / len(arr)))
    print("{:.5f}".format(pos / len(arr)))
    print("{:.5f}".format(zer / len(arr)))

#--------------------------------------------------------------------------------------------------------------------------------------
#https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem?h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def lonelyinteger(a):
    b = []
    for num in a:
        if num not in b:
            b.append(num)
        elif num in b:
            b.remove(num)
    return b[0]

#--------------------------------------------------------------------------------------------------------------------------------------
#https://leetcode.com/problems/first-missing-positive/

def firstMissingPositive(nums):
    nums.sort()
    i = 1
    repeat = 0
    for num in nums:
        if num != i and num > 0 and num != repeat:
            return i
        elif num > 0 and num != repeat:
            i += 1
        repeat = num
    return i



def main():
    
    test = "abcabcbb"
    
    print(lengthOfLongestSubstring(test))

if __name__ == "__main__":
    main()
