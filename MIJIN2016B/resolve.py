def resolve():
    '''
    code here
    '''
    import math
    arms = [int(item) for item in input().split()]

    max_l = sum(arms)
    max_seg = max(arms)
    delta = 2*max_seg - max_l

    if delta > 0:
        print(math.pi * (max_l**2 - delta**2))
    else:
        print(math.pi*max_l**2)

if __name__ == "__main__":
    resolve()
