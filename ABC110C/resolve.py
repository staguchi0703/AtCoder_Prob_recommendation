def resolve():
    '''
    code here
    '''
    N, H = [int(item) for item in input().split()]
    ab = [[int(item) for item in input().split()] for _ in range(N)]

    a_max = max(ab, key=lambda x:x[0])
    res = H // a_max
    if H % a_max != 0:
        res += 1
    
    temp_attack = res * a_max
    b_delta = [b - a_max for a, b in ab]

    throw_atk_sum = 0
    throw_num = 0

    for item in b_delta:
        if b_delta > 0:
            throw_atk_sum += item
            throw_num += 1

    if throw_atk_sum < temp_attack:
        reduce_num = throw_atk_sum//a_max
        print(res - reduce_num)
    else:
        res = 0
        for a, b in ab:
            H -= b
            res += 1
            if H <= 0:
                break
        print(res)


if __name__ == "__main__":
    resolve()
