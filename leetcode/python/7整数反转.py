class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        # print(x)
        if (x[0] == '-'):
            x = int('-' + x[:0:-1])

        else:
            x = int(x[::-1])
        if -2147483648 < x < 2147483647:
            return x
        else:
            return 0