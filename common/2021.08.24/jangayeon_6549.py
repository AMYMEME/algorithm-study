import sys
read=sys.stdin.readline

def maxSize():
    max_size = 0 #최대 넓이 저장
    stack = []

    for now in range(N):
        
        left = now
        while stack and stack[-1][0] >= heights[now]:
            
            h, left = stack.pop()
            tmp_size = h * (now-left)
            max_size = max(max_size, tmp_size)
        stack.append([heights[now],left])
   
    for h, point in stack:
        max_size = max(max_size, (N-point)*h)

    return max_size

while True:
    N, *heights = map(int,read().split())
    if N == 0: 
        break
    print(maxSize())