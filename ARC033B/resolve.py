def resolve():
    '''
    code here
    '''
    NA, NB = [int(item) for item in input().split()]

    As = [int(item) for item in input().split()]
    Bs = [int(item) for item in input().split()]

    A_memo = [0 for _ in range(10**9+1)]
    B_memo = [0 for _ in range(10**9+1)]

    for item in As:
        A_memo[item] = 1

    for item in Bs:
        B_memo[item] = 1
    
    A_and_B = []
    A_or_B = []
    for i in range(10**5+1):
        A_and_B.append(A_memo[i]&B_memo[i])
        A_or_B.append(A_memo[i]|B_memo[i])

    print(sum(A_and_B)/sum(A_or_B))



if __name__ == "__main__":
    resolve()
