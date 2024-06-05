import sys
sys.setrecursionlimit(999999999)


def main():
    N=int(input())
    S={}

    sum=0
    for _ in range(N):
        s,c=input().split()
        S[s]=int(c)
        sum+=int(c)
    
    sorted_s = sorted(S.items(), key=lambda x:x[0])
    mod_c=sum%N

    print(sorted_s[mod_c][0])

    #A=list(map(int,input().split()))
    
    #A=[]
    #for _ in range(N):
    #    A.append(list(map(int,input().split())))
    pass


if __name__ == "__main__":
    main()
