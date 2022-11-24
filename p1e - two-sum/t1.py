class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j and num + num2 == target:
                    ans = [i, j]
                    ans.sort()
                    return ans
        return [-1, -1]

print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))
