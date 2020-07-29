def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(item) for item in input().split()]
    As.sort()

    res = 0

    for i in range(1, N):
        res += As[N-1 - i//2]        

    print(res)

if __name__ == "__main__":
    resolve()
