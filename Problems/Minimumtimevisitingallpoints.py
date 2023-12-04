class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        time=0
        for i in range(len(points)-1):
            time+=max(points[i][0]-points[i+1][0],points[i][1]-points[i+1][1])
        return time
points = [[1,1],[3,4],[-1,0]]
solution1=Solution()
x=solution1.minTimeToVisitAllPoints(points)
print(x)
'''
Formula=max(y2-y1,x2-x1)
Chebyshev distance is generally a useful distance measurement in games that allow unrestricted 8-way movement,
where moving diagonally costs no more than moving in a cardinal direction.
'''