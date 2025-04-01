 
def stock_profit(prices):  
    minimum = prices[0]
    max_profit = 0
    buy_day = 0
    sell_day = 1
    
    for day, price in enumerate(prices): 
        if minimum > price: 
            minimum = price 
            buy_day = day 
            
        if max_profit < (price - minimum): 
            max_profit = price - minimum 
            sell_day = day
        
    if max_profit == 0: 
        print('Buy on day -1, sell on day -1, and make a profit of 0.') 
    else:
        print(f'Buy on day {buy_day}, sell on day {sell_day}, and make a profit of {max_profit}.')
    
   

if __name__ == '__main__': 
    
    price_str_list = input().split()
    price_list = []
    
    for price in price_str_list: 
        price = int(price) 
        price_list.append(price)  

    stock_profit(price_list) 