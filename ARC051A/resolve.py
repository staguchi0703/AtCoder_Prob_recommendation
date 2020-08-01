def resolve():
    '''
    code here
    '''
    import math
    x1, y1, r = [int(item) for item in input().split()]
    x2, y2, x3, y3 = [int(item) for item in input().split()]

    # Red
    if x2 <= x1 -r and x1 + r <= x3 and y2 <= y1 - r and y1 + r <= y3:
        print('NO')
    else:
        print('YES')
    
    # Blue
    lu = (x2-x1)**2 + (y3-y1)**2 < r**2
    ru = (x3-x1)**2 + (y3-y1)**2 < r**2
    ld = (x2-x1)**2 + (y2-y1)**2 < r**2
    rd = (x3-x1)**2 + (y2-y1)**2 < r**2

    if lu and ru and ld and rd:
        print('NO')
    else:
        print('YES')
if __name__ == "__main__":
    resolve()
