class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


def test(height): #Idea: have a buffer variabel. After added to the buffer check if there is a right wall. If there is a right wall -> Add to sum
    #OOO another idea. one more for loop that goes reverse to clear water that is wrong
    left_wall = 0
    total_water = 0
    for i in height:
        if left_wall < i:
            left_wall = i
        elif left_wall > i:
            total_water -= left_wall - i
    height.reverse()
    left_wall = 0
    for i in height:
        if left_wall < i:
            left_wall = i
        elif left_wall > i:
            total_water += left_wall - i

    return total_water

print(test([4,2,0,3,2,5]))
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""