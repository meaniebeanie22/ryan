def stock_profit(prices):
    minimum = prices[0]
    max_profit = 0
    buy_day = -1
    sell_day = -1

    for day, price in enumerate(prices):
        if minimum > price:
            minimum = price
            buy_day = day

        if max_profit < (price - minimum):
            max_profit = price - minimum
            sell_day = day

    return {"buy_day": buy_day, "sell_day": sell_day, "max_profit": max_profit}


if __name__ == "__main__":

    price_list = input().split()
    price_list = [int(x) for x in price_list]

    results = stock_profit(price_list)
    print(
        f"Buy on day {results["buy_day"]}, sell on day {results["sell_day"]}, and make a profit of {results["max_profit"]}."
    )
