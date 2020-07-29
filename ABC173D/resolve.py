def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(item) for item in input().split()]

    # 大きい順にリストにする
    # 入れ物リストを作って、大きい順に最適な位置に入れる
    # 最適な位置は最初はindex=0,
    #　次は N//2 
    #　次は連続した空席の数nに対して n//2の位置
    # 全部埋め尽くすまで居れていく

if __name__ == "__main__":
    resolve()
