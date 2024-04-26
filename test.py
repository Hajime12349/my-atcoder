import sys
import math
sys.setrecursionlimit(999999999)

li = [[1,4,3],[2,3,4],[3,4,5],[4,5,6],[2,3,4],[1,5,3],[2,3,4],[5,6,7]]
li = sorted(li, reverse=True, key=lambda x: x[0])  #[1]に注目してソート
print(li)