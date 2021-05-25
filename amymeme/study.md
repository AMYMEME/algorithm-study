## BFS(Breadth First Search)
BFS의 개념은 패스하고, 기본 작동 방식은 `queue`와 `while`을 이용한다.  
지금 위치에서 갈 수 있는 것들을 모두 큐에 넣고, 그래프라면 큐에 넣을 시점에 해당 노드를 방문했다고 체크한다.  

또한, 큐를 리스트로 구현하는 것보다는 `collections` 모듈의 `deque`를 사용하는 게 낫다고 한다.  
리스트는 실제 자료구조상 stack 처럼 동작하여 pop(0)도 O(N)의 시간 복잡도를 가진다고 한다.  

```python
from collections import deque

def bfs(graph, start_node):
    visit = set()
    queue = deque()
    
    queue.append(start_node)

    while queue :
        node = queue.pop()
        if node not in visit:
            visit.add(node)
            for nextNode in graph[node]:
                queue.append(nextNode) # 자식 노드를 큐에 추가
    return visit
```

## DFS(Depth First Search)
DFS의 기본 작동 방식은 `stack`을 이용하는데, 직접적으로 `stack`을 이용하기 보다
첫쨰줄에 `if`문으로 조건을 검사하여 `break`를 하거나 `return`으로 종료하고, 
`else`문에 재귀적으로 자신을 호출하는 형태로 이루어진다.

 ```python
def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.add(n)
            stack += graph[n]
    return visited
```

## `우선순위 큐`
> 우선순위 큐는 일반적인 FIFO 큐와 달리, 데이터 추가는 어떤 순서로 해도 상관없지만,
> 제거될 떄는 가장 작은 값을 제거하는 자료구조이다.

python의 heapq 모듈로 구현되어 있고, `from quere import PriorityQueue`로 사용할 수 있다.  
최대 크기를 가진 pq가 필요하다면, `PriorityQueue(maxsize=10)`이렇게 사용하면 된다.  
`(우선순위, 값)` 튜플로 데이터를 추가하고, 단순 오름차순이 아닌 다른 기준으로 원소가 정렬됨


## `힙`
힙은 최소힙, 최대힙이 있으며, 우선순위 큐에서 get하는 것은, min heap에서 루트를 뽑는 것과 같다.  
위의 priorityQueue 모듈보다는 heapq가 더 많이 쓰이는 것 같다.
min heap에서는 원소들이 항상 정렬된 상태로 추가되고 삭제되며,
가장 작은 ㄱ밧은 언제나 인덱스 0인 루트에 위치한다.
```python
heap[k] <= heap[2*k + 1] and head[k] <= heap[2*k + 2]
```
내장 모듈인 `import heapq`을 쓰면, 보통 리스트를 최소 힙으로 이용할 수 있다.
`heapq` 모듈 함수를 호출할 때마다 이 리스트를 인자로 넘겨주면 된다.

```python
mylist = []
heapq.heappush(mylist, 4)
heapq.heappop(mylist)
new_list = [1,6,3,8,5,5,3,8,9]
heapq.heapfity(new_list) # O(N)
```
최대 힙을 사용하려면, 튜플을 이용해야 하고, `prioirityQueue` 처럼 `(우선순위, 값)` 형태로 넣으면 된다.

### `힙 정렬`
```python
import heapq

def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums
```

### `트리`
파이썬에서 트리는 클래스로 구현할 수 있다.
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```
```python
class Tree:
    def __init__(self):
        self.root = None

    def preorder(self, node):
        print(node.data, end=' ')
        if node.left is not None:
            self.preorder(node.left)
        if node.right is not None:
            self.preorder(node.right)

    def inorder(self, node):
        if node.left is not None:
            self.inorder(node.left)
        print(node.data, end=' ')
        if node.right is not None:
            self.inorder(node.right)

    def postorder(self, node):
        if node.left is not None:
            self.postorder(node.left)
        if node.right is not None:
            self.postorder(node.right)
        print(node.data, end=' ')

    def make_root(self, node, left_node, right_node):
        if self.root:
            self.root = node
        node.left = left_node
        node.right = right_node
```