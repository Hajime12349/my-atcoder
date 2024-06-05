import sys

sys.setrecursionlimit(999999999)



def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = 10**8

    cnt = [0] * (M + 1)
    for a in A:
        cnt[a] += 1
    for i in range(M):
        cnt[i + 1] += cnt[i]

    p = 0
    for a in A:
        diff=M-a
        p+=N-cnt[diff-1]
        if a*2>=M:
            p-=1
    
    print((N-1)*sum(A)-(p//2)*M)
    pass



if __name__ == "__main__":
    main()

