def resolve():
    '''
    code here
    '''
    N = int(input())
    S = input()

    R_sum = [0 for _ in range(N)]
    G_sum = [0 for _ in range(N)]
    B_sum = [0 for _ in range(N)]

    if S[0] == 'R':
        R_sum[0] += 1
    elif S[0] == 'G':
        G_sum[0] += 1
    else:
        B_sum[0] += 1

    for i in range(1, N):
        if S[i] == 'R':
            R_sum[i] += 1
            R_sum[i] += R_sum[i-1]
        elif S[i] == 'G':
            G_sum[i] += 1
            G_sum[i] += G_sum[i-1]
        else:
            B_sum[i] += 1
            B_sum[i] += B_sum[i-1]
    # 外す条件を調べないと
    res = 0
    for k in range(1,N-1):
        if S[k] == 'R':
            res += G_sum[k-1] 




if __name__ == "__main__":
    resolve()
