'''
https://www.acmicpc.net/problem/1339
'''
import sys

N=int(sys.stdin.readline().strip())
alphabet=dict()

for _ in range(N):
    word=sys.stdin.readline().strip()
    for k,element in enumerate(word[::-1]):
        if element not in alphabet.keys():
            alphabet[element]=0
        alphabet[element]+=10**k
sort_alphabet=dict(sorted(alphabet.items(), key=lambda x : x[1] ,reverse=True))

result=0
for n,i in enumerate(sort_alphabet.values()):
    result+=(9-n)*i
print(result)