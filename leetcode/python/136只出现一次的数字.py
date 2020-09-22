class Solution:
    # 使用了额外的空间，导致时间空间都很靠后
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for i in d:
            if d[i] == 1:
                return i

    # 看了大佬解析后，使用异或法
    def singleNumber1(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            s ^= i
        return s


if __name__ == '__main__':
    nums = eval(input())
    s = Solution()
    print(s.singleNumber1(nums))
