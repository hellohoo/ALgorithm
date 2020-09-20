class Solution():
    def isPalindrome(self,x: int) -> bool:
        # 将x换成str形式
        x = str(x)
        # print(x[::-1])
        # print(x[::1])
        if(x[::-1]==x[::1]):
            return True
        else:
            return False

if __name__ == '__main__':
    x = eval(input())
    s = Solution()
    print(s.isPalindrome(x))