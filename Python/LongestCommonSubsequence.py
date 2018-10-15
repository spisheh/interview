"""
A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. Longest common subsequence (LCS) of 2 sequences is a subsequence, with maximal length, which is common to both the sequences. 

Given two sequence of integers,  and , find any one longest common subsequence.

In case multiple solutions exist, print any of them. It is guaranteed that at least one non-empty common subsequence will exist.

Input Format

First line contains two space separated integers,  and , where  is the size of sequence , while  is size of sequence . In next line there are  space separated integers representing sequence , and in third line there are  space separated integers representing sequence .

n m
A1 A2 … An 
B1 B2 … Bm  
Constraints

 
 
 

Output Format

Print the longest common subsequence and each element should be separated by at least one white-space. In case of multiple answers, print any one of them.

Sample Input

5 6
1 2 3 4 1
3 4 1 2 1 3
Sample Output

1 2 3
Explanation

There is no common subsequence with length larger than 3. And "1 2 3", "1 2 1", "3 4 1" are all correct answers.
"""

n,m = map(int, input().split())
arr1= input().split()
arr2= input().split()


lst = [[]]*m

for col in range(m):
    if arr1[0]==arr2[col]:
        lst[col]=[arr1[0]]

for row in range(1,n):
    new=[[]]*m
    for col in range(m):
        if col==0:
            if arr1[row]==arr2[col]:
                new[col]=[arr1[row]]
            else:
                new[0]=lst[0]
        elif arr1[row]==arr2[col]:
            #print(arr1[row])
            new[col]=max( lst[col-1]+[arr1[row]], lst[col]+[], new[col-1]+[], key = lambda a : len(a))
        else:
            new[col]=max( lst[col-1]+[], lst[col]+[], new[col-1]+[], key = lambda a : len(a))
    lst=new
print(" ".join(lst[-1]))