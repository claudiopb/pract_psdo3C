def sum_range(k):
  if k > 0:   # base case
    print(k)	
    return k + sum_range(k - 1)
  else:
    return 0

result = sum_range(2)
print(result)   # 55
