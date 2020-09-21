class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 将数字列表转换为str，再str转换为int后+1，最后将int转换为str后分割成int列表
        x = []
        s = ""
        for i in digits:
            s += str(i)
        s = int(s)
        s = s + 1
        s = str(s)
        for i in s:
            x.append(int(i))
        return x


if __name__ == '__main__':
    x = []
    s = Solution()
    digits = [1, 2, 3]
    x = s.plusOne(digits)
    print(x)
