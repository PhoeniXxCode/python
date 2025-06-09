def maxprofit(prices):
    min_price = float('inf')   # Initialize to infinity
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    
    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(maxprofit(prices))  # Output: 5
