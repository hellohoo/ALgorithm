class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # 使用栈
        d = {'(': ')', '[': ']', '{': '}'}

        for c in s:
            if c in d:
                stack.append(c)  # 左括号入栈
            elif stack:  # 如果碰到右括号且栈不为空，则判断栈最后进入的和该括号是否配对
                if c != d[stack.pop()]:
                    return False
            else:
                return False
        return not stack  # 如果栈为空，则返回True;不为空如"({}"该情况，最后栈会为['(']，则返回Fals
if __name__ == '__main__':
    s = Solution()
    x = input()
    print(s.isValid(x))
