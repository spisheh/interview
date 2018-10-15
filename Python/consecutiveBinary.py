"""
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
Explanation

Sample Case 1: 
The binary representation of  is , so the maximum number of consecutive 's is .

Sample Case 2: 
The binary representation of  is , so the maximum number of consecutive 's is .
"""
#!/bin/python3

import math
import os
import random
import re
import sys
def  consecutiveBinary(n):

    #s=bin(n)[2:]
    maxi=0
    temp=0
    #for c in s:
    while n > 0:
        c= n % 2
        n= n//2
        if c == 1:
            temp+=1
            if temp>maxi:
                maxi=temp
        else:
            temp=0
            
    if temp>maxi:
        maxi=temp
    return maxi

if __name__ == '__main__':
    n = int(input())
    print(consecutiveBinary(n) )