'''
You're given an array prices where prices[i] is the price of a stock on day i. You want to maximize profit by choosing a single day to buy and a different day in the future to sell. Return the maximum profit. If no profit is possible, return 0.
pythonExample:
Input: prices = [7,1,5,3,6,4]
Output: 5  # buy on day 2 (price=1), sell on day 5 (price=6), profit = 6-1 = 5
'''


def buySellStock(prices):
    low = float('inf')
    profit = 0

    for price in prices:
        if price < low:
            low = price  # 1
        elif price - low > profit:
            profit = price - low

    return profit


print(buySellStock([7, 1, 5, 3, 6, 4]))
