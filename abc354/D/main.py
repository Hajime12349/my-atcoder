import sys
sys.setrecursionlimit(999999999)


def count_black_area(A, B, C, D):
        row_p=[1,0.5,0,0.5]
        line_p=[1,0.5]
        avr_row=2
        #avr_line=1.5
        
        W = C - A
        H = D - B

        #diff_X=A%
        diff_X=A%4
        mod_X=W%4



        row_num=W/4
        line_num=H
        print(row_num,line_num)
        black=line_num*(row_num*avr_row)

        addon=0
        for x in range(mod_X):
            addon+=row_p[diff_X]
        
        black+=addon

        return black


def main():
        
    # 入力の取得
    A, B, C, D = map(int, input().split())

    # 結果の出力
    print(count_black_area(A, B, C, D))
    #N=int(input())
    #S=input().split()
    #A=list(map(int,input().split()))
    
    #A=[]
    #for _ in range(N):
    #    A.append(list(map(int,input().split())))
    pass


if __name__ == "__main__":
    main()
