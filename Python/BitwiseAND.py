"""
Given set . Find two integers,  and  (where ), from set  such that the value of  is the maximum possible and also less than a given integer, . In this case,  represents the bitwise AND operator.

Input Format

The first line contains an integer, , the number of test cases. 
Each of the  subsequent lines defines a test case as  space-separated integers,  and , respectively.

Constraints

Output Format

For each test case, print the maximum possible value of  on a new line.

Sample Input

3
5 2
8 5
2 2
Sample Output

1
4
0
Explanation

 

All possible values of  and  are:

The maximum possible value of  that is also  is , so we print  on a new line.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

def binary(n,k):
    maxi=int(math.log(n-1,2))+1
    for i in range(k,-1,-1):
        for exp in range(maxi):
            plus=2**exp
            if i+plus > n:
                break
            if i | plus > i:
                return i

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print(binary(n,k-1))