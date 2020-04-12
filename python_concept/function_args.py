def mysum(*args):
    overall_sum =  0
    for elem in args:
        overall_sum += elem
    return overall_sum

print(mysum(1,2,3,4))
print(mysum(1,2))
