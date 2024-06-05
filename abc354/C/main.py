import sys
sys.setrecursionlimit(999999999)

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while (i < len(left)) and (j < len(right)):
        if left[i][0] <= right[j][0]:
            result.append(left[i])   
            i += 1
        else:
            result.append(right[j])  
            j += 1

    if i < len(left):
        result.extend(left[i:]) 
    if j < len(right):
        result.extend(right[j:])

    return result

def main():
    N=int(input())
    #S=input().split()
    #A=list(map(int,input().split()))
    
    A=[]
    for n in range(N):
        a,c=map(int,input().split())
        A.append((a,c,n))
    
    sorted_a=merge_sort(A)
    
    #print(type(A[0]))
    ans=[]
    min_c=pow(10,9)+1
    i=N-1
    while i>=0:
        #pritn(sorted_a[i])
        if min_c>sorted_a[i][1]:
            #print(sorted_a[i])
            ans.append(tuple([sorted_a[i][2]+1]))
            min_c=sorted_a[i][1]
        i-=1
    
    #print(type(ans[0]))
    sorted_ans=merge_sort(ans)
    
    print(len(ans))
    for i in range(len(sorted_ans)-1):
        print(sorted_ans[i][0],end=" ")
    print(sorted_ans[-1][0])

    pass


if __name__ == "__main__":
    main()
