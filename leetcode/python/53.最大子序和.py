class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = [0 for i in range(len(nums))]
        n[0] = nums[0]
        for i in range(1,len(nums)):
            n[i] = max(nums[i],n[i-1]+nums[i])

        return max(n)

if __name__ == '__main__':
    s = Solution()
    nums = eval(input())
    s.maxSubArray(nums)