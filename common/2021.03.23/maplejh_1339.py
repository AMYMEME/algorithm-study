'''
https://www.acmicpc.net/problem/1339
'''
import sys
from collections import defaultdict

N=int(sys.stdin.readline())
alphabet=defaultdict(int)

for _ in range(N):
    word=sys.stdin.readline().strip()
    for n,e in enumerate(word[::-1]):
        alphabet[e]+=pow(10,n)

v=sorted(alphabet.values(),reverse=True)
result=0
for n,i in enumerate(v):
    result+=(9-n)*i

print(result)