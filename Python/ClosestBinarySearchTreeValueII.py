"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?


*****************Note*****************
69 / 69 test cases passed.
Runtime: 56 ms
Runtime beats 100.00 % of python3 submissions.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq
class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        pre=[]				#contains smaller number that target in accending order
        post=[]				#contains bigger number that target in descending order
        temp=root
        while temp:
            if temp.val > target:
                post.append(temp)
                temp=temp.left
            else:
                pre.append(temp)
                temp=temp.right
         
        #find and place the biggest number on the pre array at the end       
        def left_biggest():			
            root=pre.pop().left
            while root:
                pre.append(root)
                root = root.right
        #find and place the smallest number on the post array at the end    
        def right_smallest():
            root=post.pop().right
            while root:
                post.append(root)
                root = root.left
                
        res=[]
        while len(res)<k:
            if not pre or (post and post[-1].val-target < target-pre[-1].val):
                res.append(post[-1].val)
                right_smallest()
            elif pre:
                res.append(pre[-1].val)
                left_biggest()
            elif not pre and not post:
                print("these are not enough numbers in the tree")
                break
        return res
        