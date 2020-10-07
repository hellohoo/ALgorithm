class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(" ").split(" ")
        if s:
            return len(s[-1]) 
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    str = input()
    print(s.lengthOfLastWord(str))