import io
import sys

_INPUT = """\
6
5
1 5
3
3 4 2
7
1 3
4
2 4 2 7
4
1 4
3
2 1 3
4
1 4
3
2 4 3
20
1 4
12
2 3 5 7 8 9 10 11 12 15 13 14
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  a,b=map(int,input().split()) 
  K=int(input())
  P=list(map(int,input().split()))
  if a in set(P) or b in set(P) or len(set(P))<K: print('NO')
  else: print('YES')