def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    Rs = [int(item) for item in input().split()]

    Rs.sort()
    res = 0

    for i in range(N-K, N):
        res = (res + Rs[i])/2


    print(res)


if __name__ == "__main__":
    resolve()
