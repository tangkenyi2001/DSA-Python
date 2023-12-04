class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,values in enumerate(nums):
            if values in dict:
                dict[values].append(i)
            else:
                dict[values]=[i]
        for j in nums:
            x=target-j
            if x in dict:
                if dict[j]==dict[x] and len(dict[x])!=1:
                    return [dict[x][0],dict[x][1]]
                if dict[j]!=dict[x]:
                    return [dict[j][0],dict[x][0]]
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,values in enumerate(nums):
            integerneeded=target-values
            if integerneeded in dict:
                return [dict[integerneeded],i]
            dict[values]=i