class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 设计深拷贝浅拷贝切片
        nums[:] = list(sorted(set(nums)))
        return len(nums)

if __name__ == '__main__':
    s = Solution()
    nums = eval(input())
    print(s.removeDuplicates(nums))