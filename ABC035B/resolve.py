def resolve():
    '''
    code here
    '''
    import collections
    S = [item for item in input()]
    T = int(input())

    letter_cnt = collections.Counter(S)

    res = 0
    cnt_que = letter_cnt['?']
    x = letter_cnt['R'] - letter_cnt['L']
    y = letter_cnt['U'] - letter_cnt['D']

    if T ==1:
        res = abs(x) + abs(y) + cnt_que
    else:
        temp_deff = abs(x) + abs(y) - cnt_que

        if temp_deff >= 0:
            res = temp_deff
        else:
            res = abs(temp_deff) % 2

    print(res)

if __name__ == "__main__":
    resolve()
