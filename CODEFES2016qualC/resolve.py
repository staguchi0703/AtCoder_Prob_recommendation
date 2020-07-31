def resolve():
    '''
    code here
    '''
    import collections
    K , T = [int(item) for item in input().split()]
    As = [int(item) for item in input().split()]
    As.sort(reverse=True)

    cnt = collections.Counter(As)
    interval_num = As[0]-1

    res = interval_num - sum(As[1:])

    if res <= 0:
        print(0)
    else:
        print(res)

if __name__ == "__main__":
    resolve()
