#https://www.acmicpc.net/problem/15927




word=input().strip()
word_reverse=''.join(reversed(word))
#회문인 경우
if word !=(word_reverse): #원래 글자와 뒤집은 글자가 같은 경우
    ans=len(word)
elif len(set(word)) == 1: #모두 다 같은 문자로 이루어진 경우
    ans= -1
#회문인 아닌 경우
else: 
    ans=len(word) - 1

print(ans)

