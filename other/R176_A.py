import sys
sys.setrecursionlimit(999999999)

#n=int(input())


N,M=map(int,(input().split()))

M_ab=[]
for m in range(M):
    a,b=map(int,(input().split()))
    M_ab.append((a-1,b-1))


ans=[]
A=[[0]*N for _ in range(N)]
for m in range(M):
    for n in range(N):
        offset_index=(n+m)%N
        #print(offset_index)
        A[offset_index][n]=1
        ans.append((offset_index,n))

for m_ab in M_ab:
    a,b=m_ab
    #print(type(a),type(b))
    delete_line=N+1 #エラーを吐く初期値
    if(A[a][b]==0):
        ans.append((a,b))
        for n in range(N):
            if A[n][b]==1:
                A[n][b]=0
                delete_line=n
                ans.remove((n,b))
                break
        for n in range(N):
            if A[a][n]==1 and A[delete_line][n]==0:
                A[delete_line][n]=1
                ans.remove((a,n))
                ans.append((delete_line,n))
                #print(a,delete_line,n)
                #print(ans)
                break

print(len(ans))
for ans_i in ans:
    print(ans_i[0]+1,ans_i[1]+1)

            
#a=list(map(int,input().split()))
