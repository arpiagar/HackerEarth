def mykwargs(**kwargs):
    overall_sum =  0
    import pdb;pdb.set_trace()
    print(kwargs)
    for args in kwargs:
        print(args)

print(mykwargs(name=2,birth=4))
print(mykwargs(name=2))
