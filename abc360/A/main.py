import sys
sys.setrecursionlimit(999999999)


def main():
    #N=int(input())
    S=input()
    #A=list(map(int,input().split()))
    
    #A=[]
    #for _ in range(N):
    #    A.append(list(map(int,input().split())))
    
    for s in S:
        if s=="R":
            print("Yes")
            break
        elif s=="M":
            print("No")
            break
    
    pass


if __name__ == "__main__":
    main()
