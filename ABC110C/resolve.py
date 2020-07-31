def resolve():
    '''
    code here
    '''
    import collections
    S = [item for item in input()]
    T = [item for item in input()]

    S_cnt = collections.Counter(S)
    T_cnt = collections.Counter(T)


    if sorted(S_cnt.values()) == sorted(T_cnt.values()):
            print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    resolve()
