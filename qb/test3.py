def drawingEdge(n):
    var1 = (n*(n-1))//2
    answer = pow(2, var1)
    print("ans",answer, var1,n)
    return answer
    # Write your code here

if __name__ == '__main__':
    for i in range(2,5):

        print(i,":",drawingEdge(i))
