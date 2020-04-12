def numberOfWays(n):
    hash_map = {0:0, 1:1, 2:1, 3:2}
    val = numberOfWaysOptimized(n, hash_map)
    return val

def numberOfWaysOptimized(n, hash_map):
    if n in hash_map:
        return hash_map[n]
    value = numberOfWaysOptimized(n-1,hash_map) + numberOfWaysOptimized(n-3, hash_map)
    hash_map[n] = value % 1000000007
    print(hash_map)
    return hash_map[n]
if __name__ == '__main__':
    print(numberOfWays(13))
    #for i in range(0, 20):
    #    print(numberOfWays(i))
