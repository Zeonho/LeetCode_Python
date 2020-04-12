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
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

class Solution:
    def gcd(self,a,b):
        if(b==0):
            return a
        else:
            return self.gcd(b,a%b)

    def maxPoints(self, points: List[List[int]]) -> int:
        maxNumOfPoints = 0
        for i in range(len(points)):
            table = {'90' : 1}
            samePoint = 0
            for j in range(i+1, len(points)):
                if(points[i][0] == points[j][0] and points[i][1] == points[j][1]):
                    samePoint += 1
                    continue
                if(points[i][0] == points[j][0]):
                    angle = '90'
                else:
                    temp = self.gcd(points[i][1]-points[j][1], points[i][0]-points[j][0])
                    angle = ((points[i][1]-points[j][1])/temp, (points[i][0]-points[j][0])/temp)
                    #angle = (points[i][1]-points[j][1]) * 1.0 /(points[i][0]-points[j][0])
                if(angle not in table):
                    table[angle] = 1
                table[angle] += 1
            maxNumOfPoints = max(maxNumOfPoints, max(table.values()) + samePoint)
        if(len(points) == 0):
            return 0
        #print table
        return maxNumOfPoints 