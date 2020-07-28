def resolve():
    '''
    code here
    '''
    import collections
    N = int(input())
    S = input()

    cnt_dict = collections.Counter([item for item in S])
    ng_cnt = 0
    for i in range(N):
        for j in range(i, N):
            k = 2*j - i
            if k < N:
                if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
                    ng_cnt += 1
    
    print(cnt_dict['R']*cnt_dict['G']*cnt_dict['B'] - ng_cnt)


if __name__ == "__main__":
    resolve()
