# Enter your code here. Read input from STDIN. Print output to STDOUT
#Hackerrank: https://www.hackerrank.com/challenges/chief-hopper


def calc_ene(n,n_list):
    ene = 0
    for i in xrange(n-1,-1,-1):
        if (ene+n_list[i])%2 == 1:
            ene = (ene+n_list[i])/2 + 1
        else:
            ene = (ene+n_list[i])/2 
    return ene
n =  int(raw_input())
n_list = raw_input().split(" ")
n_list = [int(x) for x in n_list]
print calc_ene(n,n_list)