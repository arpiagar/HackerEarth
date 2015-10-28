def find_max_stock_price(stock_price_list):
  """ Function to find the max profit in single purchase and sell of stocks"""
  num_entries =  len(stock_price_list)
  if num_entries == 0:
     return 
  minimum =  stock_price_list[0]
  min_idx = 0
  sell_idx = 0
  profit = 0
  for i in xrange(1, num_entries):
    new_profit = stock_price_list[i] - minimum
    if new_profit > profit:
      profit = new_profit
      sell_idx = i + 1
      new_min_idx = min_idx
    if minimum > stock_price_list[i]:
      minimum =  stock_price_list[i]
      min_idx = i + 1
  print profit,new_min_idx,sell_idx

input_list = [23,34,45,7,33,34,22,5]
find_max_stock_price(input_list)