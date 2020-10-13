class Solution:
    def rob(self, nums) -> int:
        summ = [0 for i in range(len(nums) + 1)]
        summ[1] = nums[0]
        i = 1
        for j in range(1, len(nums)):
            # print(summ[j], summ[j - 1] + nums[i])
            summ[j + 1] = max(summ[j], summ[j - 1] + nums[i])
            i += 1
        # print(summ)
        return summ[-1]


if __name__ == '__main__':
    s = Solution()
    nums = eval(input())
    # nums = [2,1,1,2]
    print(s.rob(nums))
