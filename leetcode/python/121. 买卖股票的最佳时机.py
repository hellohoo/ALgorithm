class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_d = float('inf')  # 正无穷
        if len(prices) < 2:
            return 0
        for i in range(len(prices) - 1):
            if prices[i] > prices[i + 1]:  # 判断后一个是否比自己小，如果小的话就继续
                continue
            if prices[i] < min_d:  # 判断该天price是否比最小天的price还小
                min_d = prices[i]
                for j in range(i + 1, len(prices)):  # 和该天后的价格直接比较
                    max_prof = max(max_prof, prices[j] - prices[i])  # 比较出最max的
        return max_prof if max_prof > 0 else 0


if __name__ == '__main__':
    s = Solution()
    prices = [3, 5, 2, 6, 7]
    print(s.maxProfit(prices))
