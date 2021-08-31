class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        num = sorted(list(set(nums)))
        res = len(num)
        for i in range(len(nums)):
            if i<res:
                nums[i] = num[i]
            else:
                nums[i] = '_'
        return res

S = Solution()
S.removeDuplicates([1,1,2])