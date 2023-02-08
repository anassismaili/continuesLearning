def coinChange(self, coins: List[int], amount: int) -> int:

    if amount == 0 or coins is None or len(coins) == 0:
        return 0
    numbers = [0] * (amount + 1)
    for coin in coins:
        for i in range(coin, amount + 1):
            if i == coin:
                numbers[i] = 1
            elif numbers[i] == 0 and numbers[i - coin] != 0:
                numbers[i] = numbers[i - coin] + 1
            elif numbers[i - coin] != 0:
                numbers[i] = min(numbers[i], numbers[i - coin] + 1)
                
    return -1 if numbers[amount] == 0 else numbers[amount]