def resolve():
    '''
    code here
    '''
    from bisect import bisect_left as bis
    NA, NB = [int(item) for item in input().split()]

    As = [int(item) for item in input().split()]
    Bs = [int(item) for item in input().split()]
    Bs.sort()
    
    cnt_A_and_B = 0
    for item in As:
        b_index = bis(Bs, item)
        if b_index < NB: 
            if item == Bs[b_index]:
                cnt_A_and_B +=1

    cnt_A_or_B = len(set(As+Bs))
        

    print(cnt_A_and_B/cnt_A_or_B)



if __name__ == "__main__":
    resolve()
