class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        B = []

        for j in range(len(A[0])):
            c = []
            for i in range(len(A)):
                c.append(A[i][j])
            B.append(c)

        return B
if __name__ == '__main__':
    s = Solution()
    A = eval(input())
    print(s.transpose(A))
