class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 大神写法，用zip函数，牛逼
        a = ''
        for i in zip(*strs):
            if len(set(i))==1:
                a += i[0]
            else:
                break
        return a

if __name__ == '__main__':
    s = Solution()
    strs = eval(input())
    print(s.longestCommonPrefix(strs))