'''
https://www.acmicpc.net/problem/4949
'''
import sys

def check(a):
    stack=[0]
    for i in a:
        if i=="(" or i=="[":
            stack.append(i)
        elif i==")" and stack[-1]=="(":
            stack.pop()
        elif i=="]" and stack[-1]=="[":
            stack.pop()
        else:
            return "no"
    return "yes" if len(stack)==1 else "no" 

if __name__ == "__main__":
    input=sys.stdin.readline
    while True:
        string=input().rstrip()
        a=[]
        if string==".":
            break
        for s in string:
            if s in '()[]':
                a.append(s)
        if len(a)==0: 
            print("yes")
        else:
            print(check(a))