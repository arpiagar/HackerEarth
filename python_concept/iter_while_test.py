list1=[1,2,3,4]
iter1=iter(list1)

try:
    while iter1:
        print(next(iter1))
except StopIteration:
    pass
print("Completed succesfully")
