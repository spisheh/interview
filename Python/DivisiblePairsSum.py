"""
You are given an array of  integers, , and a positive integer, . Find and print the number of  pairs where  and  +  is evenly divisible by .

Input Format

The first line contains  space-separated integers,  and , respectively. 
The second line contains  space-separated integers describing the respective values of .

Constraints

Output Format

Print the number of  pairs where  and  +  is evenly divisible by .

Sample Input

6 3
1 3 2 6 1 2
Sample Output

 5
Explanation

Here are the  valid pairs:


"""



import math
import os
import random
import re
import sys

def findPair(arr,k):
    dict={}
    count=0
    for i,e in enumerate(arr):
        m = e % k
        comp = ( k-m ) % k
        if comp in dict:
            count+=dict[comp]
        dict[m]=dict.get(m,0)+1
    return count


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    a = list(map(int, input().rstrip().split()))
    print(findPair(a,k))

