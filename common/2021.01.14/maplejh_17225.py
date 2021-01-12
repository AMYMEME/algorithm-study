'''
https://www.acmicpc.net/problem/17225
'''

import sys

s_flag, j_flag =0 ,0  # 상민/지수가 앞 주문을 끝나는 시간
A,B,N=map(int,sys.stdin.readline().split())
timeline=[]

for n in range(N):
    o_time, o_color, o_num=sys.stdin.readline().split()
    o_time, o_num=int(o_time), int(o_num)
    if o_color=='B':
        start_time=s_flag if s_flag>o_time else o_time
        s_flag=start_time+o_num*A
        speed,color=A,1
    elif o_color=='R':
        start_time=j_flag if j_flag>o_time else o_time
        j_flag=start_time+o_num*B
        speed,color=B,2
    for m in range(o_num):
        timeline.append((start_time+speed*m,color))

timeline=sorted(timeline)

present_num=0
B=[]
R=[]
for (t,n) in timeline:
    present_num+=1
    if n==1:
        B.append(present_num)         
    elif n==2:
        R.append(present_num)
print(len(B))
print(" ".join(map(str,B)))
print(len(R))
print(" ".join(map(str,R)))