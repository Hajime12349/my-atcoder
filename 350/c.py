import sys

sys.setrecursionlimit(999999999)


def merge_sort(A,idx):
    half_idx=int(len(A)/2)
    if half_idx==0:

        return A,[]

    a_left=A[:half_idx]

    a_right=A[half_idx:]

    #print(a_left)

    sort_left,ans_l=merge_sort(a_left,idx)

    sort_right,ans_r=merge_sort(a_right,idx+half_idx)

    ans=ans_l+ans_r

    sorted_A,ans=merge(sort_left,sort_right,ans,idx)

    return sorted_A,ans


def merge(left,right,ans,idx):

    idx_r=0

    idx_l=0
    len_l=len(left)
    len_r=len(right)
    sorted_list=[]

    while idx_l<len_l and idx_r<len_r:

        if right[idx_r]>left[idx_l]:

            sorted_list.append(left[idx_l])

            idx_l+=1

        else:

            sorted_list.append(right[idx_r])

            ans.append((idx+idx_l+1,idx+len_l+idx_r+1))

            tmp=right[idx_r]
            right[idx_r]=left[idx_l]

            left[idx_l]=tmp

            #print(ans[-1])

            idx_r+=1

            idx_l+=1

    sorted_list=sorted_list+left[idx_l:]+right[idx_r:]

    #print(sorted_list)

    return sorted_list,ans

         


N=int(input())

A=list(map(int,input().split()))
ans=[]


A_ans,ans=merge_sort(A,0)


#print(A_ans)

print(len(ans))
for ans_i in ans:
    print(f'{ans_i[0]} {ans_i[1]}')



