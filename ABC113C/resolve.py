def resolve():
    '''
    code here
    '''
    N, M = [int(item) for item in input().split()]
    PY = [[int(item) for item in input().split()] for _ in range(M)]

    memo = [[] for _ in range(N+1)]

    for p, y in PY:
        memo[p] += [y]

    res_list = []
    for lst in memo:
        lst.sort()
        temp_dic = dict(zip(lst, range(1,len(lst)+1)))
        res_list.append(temp_dic)

    for p, y in PY:
        pi = str(p).zfill(6)
        x = str(res_list[p][y]).zfill(6)
        print(pi+x)


if __name__ == "__main__":
    resolve()
