def resolve():
    '''
    code here
    '''
    C = int(input())
    laggages = [sorted([int(item) for item in input().split()]) for _ in range(C)]
    N, L, M = 0, 0, 0

    for n, l, m in laggages:
        N = max(N, n)
        L = max(L, l)
        M = max(M, m)
    
    print(N*L*M)
if __name__ == "__main__":
    resolve()
