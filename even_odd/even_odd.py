def even_odd(ip, n):
  start = 0
  end = n-1
  while start< end:
    if ip[start]%2 !=0:
      start += 1
    else:
      ip = swap(ip,start,end)
      end -= 1
  return ip

def swap(ip,s,e):
  temp = ip[s]
  ip[s] = ip[e]
  ip[e] = temp
  return ip
ip = [2, 4, 1, 3, 5, 6, 7, 3, 5]
print even_odd(ip, len(ip))