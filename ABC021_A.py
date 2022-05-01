import io
import sys

_INPUT = """\
6
5
1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  print(N)
  for i in range(N): print(1)