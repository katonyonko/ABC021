import io
import sys

_INPUT = """\
6
10
2
10
3
10
4
400
296
100000
100000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=10**9+7
  n=int(input())
  k=int(input())
  F=[1]
  for i in range(n+k):
      F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(n+k):
      I.append(I[-1]*(n+k-i)%mod)
  I=I[::-1]
  print(F[n+k-1]*I[n-1]*I[k]%mod)