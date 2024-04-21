import sys
sys.setrecursionlimit(999999999)

s=input()
t=input()

t=t.lower()
s_len=len(s)
prev_index=0

ans=True
count=0

for ti in t:
    count+=1
    index=0
    judge=False
    for si in s[prev_index:]:
        index+=1
        #print(f'({ti}:{si},{index})')
        
        if si==ti:
            prev_index+=index
            judge=True
            break
    
    #print(f'{index}+{prev_index}')
    if not judge:
        if ti=='x' and count==3:
            #print("ok")
            break
        ans=False
        break

if ans:
    print("Yes")
else:
    print("No")
