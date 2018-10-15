"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6


**********************************
36 / 36 test cases passed.
Runtime: 52 ms
Runtime beats 98.60 % of python3 submissions.
"""

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """ 

        
        #get the slope of to points
        def slope(p1,p2):
            if p1[0]==p2[0]:
                return (float("inf"), p1[0])
            else:
                m=(p1[1]-p2[1])/(p1[0]-p2[0])
                b= p1[1]-m*p1[0]
                return (m, b)
            
            
        #considering the same points as weights 
        points_weight={}
        for p in points:
            points_weight[(p.x,p.y)]=points_weight.get((p.x,p.y),0)+1
            


        points = list(points_weight.keys())
        size=len(points)
        if size < 3:
            return sum([points_weight[p] for p in points])
        count=0			#counting the number of point passing from each line
        for i in range(size-1):
            lines={}
            for j in range(i+1,size):
                slp=slope(points[i], points[j])
                lines[slp]=lines.get(slp, points_weight[points[i]])+ points_weight[points[j]]
                if lines[slp]>count:
                    count=lines[slp]

        return count
