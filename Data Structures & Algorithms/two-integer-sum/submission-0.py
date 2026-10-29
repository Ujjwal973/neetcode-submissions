class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        start = 1
        for i in range(len(nums)-1):
            for j in range(start,len(nums)):
                if (nums[i] + nums[j]) == target:
                    solution.append(i)
                    solution.append(j)
            start +=1
        return solution