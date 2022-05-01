import io
import sys

_INPUT = """\
6
7
1 7
8
1 2
1 3
4 2
4 3
4 5
4 6
7 5
7 6
7
1 7
9
1 2
1 3
4 2
4 3
4 5
4 6
7 5
7 6
4 7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=10**9+7
  N=int(input())
  a,b=map(int,input().split())
  a-=1; b-=1
  M=int(input())
  G=[[] for _ in range(N)]
  for i in range(M):
    x,y=map(int,input().split())
    x-=1; y-=1
    G[x].append(y)
    G[y].append(x)
  from collections import deque
  def bfs(G,s):
    inf=10**30
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D
  D=bfs(G,a)
  memo=[-1]*N
  memo[a]=1
  def rec(k):
    if memo[k]!=-1: return memo[k]
    memo[k]=0
    for v in G[k]:
      if D[v]==D[k]-1: memo[k]=(memo[k]+rec(v))%mod
    return memo[k]
  print(rec(b))