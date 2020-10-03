class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        n = bin(n).lstrip('0b')
        # print(n)
        # print(type(n))
        for i in str(n):
            if i == '1':
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    n = eval(input())
    print(s.hammingWeight(n))
