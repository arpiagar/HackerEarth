def find_fibo_count(n):
  fibo_0 = 0
  fibo_1 = 1

  if n ==0:
  	return 0
  if n==1:
  	return 1

  count = 3
  t1 = 1
  t2 = 1
  while True:
    t3 = t1+t2
    count += 1
    if t3 > n:
      print "break"
      break
    print "continue.."
    t1 = t2
    t2 = t3
  return count

print find_fibo_count(5)
print find_fibo_count(10)
print find_fibo_count(15)


0 1 1 2 3 5 8