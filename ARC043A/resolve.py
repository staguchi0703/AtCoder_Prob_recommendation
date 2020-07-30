def resolve():
    '''
    code here
    '''
    N, A, B = [int(item) for item in input().split()]
    Ss = [int(input()) for _ in range(N)]

    delta = max(Ss) - min(Ss)

    try:
        p = B / delta
        q = -1*sum(Ss)/N * p + A

        print(p, q)
    except:
        print(-1)

if __name__ == "__main__":
    resolve()
