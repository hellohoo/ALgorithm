class Solution:
    '''
    利用增加了一个list来存储数据，很笨拙的方法，一看就懂，就是C这块的代码改了两次，
    刚开始觉得直接j-2覆盖掉C前的数字开始重新写，但发现当C在数列最末尾时，是不会有内容来覆盖的，
    因为是求和，所以直接用0代替C前的位置并且如果C后有内容可以直接覆盖
    '''
    def calPoints(self, ops: List[str]) -> int:
        x = [0 for i in range(len(ops))]
        sum = 0
        j = 0
        for i in range(len(ops)):
            if ops[i].isdigit() == True or ops[i][0] == '-':
                x[j] = int(ops[i])

            if ops[i] == 'C':
                x[j - 1] = 0
                j = j - 2
            if ops[i] == 'D':
                x[j] = x[j - 1] * 2

            if ops[i] == '+':
                x[j] = x[j - 1] + x[j - 2]
            j += 1
            # print(x)
        for i in x:
            sum += i

        return sum
if __name__ == '__main__':
    s = Solution()
    ops = eval(input())
    print(s.calPoints(ops))