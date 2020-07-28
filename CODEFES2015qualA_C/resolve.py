def resolve():
    '''
    code here
    '''
    N, T = [int(item) for item in input().split()]
    duteis = [[int(item) for item in input().split()] for _ in range(N)]
    Bs = [item[1] for item in duteis]
    Cs = [item[0] - item[1] for item in duteis]
    Cs.sort()

    if sum(Bs) <= T:
        T -= sum(Bs)
        res = N
        
        for item in Cs:
            T -= item
            if T >= 0:
                res -= 1
            else:
                break

    else:
        res = -1

    print(res)

if __name__ == "__main__":
    resolve()
