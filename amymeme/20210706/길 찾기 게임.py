# https://programmers.co.kr/learn/courses/30/lessons/42892
# 길 찾기 게임
import sys


class Node:
    def __init__(self, x, node_id):
        self.node_id = node_id
        self.x = x
        self.left = None
        self.right = None

    def insert(self, x, node_id):
        if self.x > x:
            if self.left is None:
                self.left = Node(x, node_id)
            else:
                self.left.insert(x, node_id)
        else:
            if self.right is None:
                self.right = Node(x, node_id)
            else:
                self.right.insert(x, node_id)

    def pre_order(self):
        global pre_result
        pre_result.append(self.node_id)
        if self.left is not None:
            self.left.pre_order()
        if self.right is not None:
            self.right.pre_order()

    def post_order(self):
        global post_result
        if self.left is not None:
            self.left.post_order()
        if self.right is not None:
            self.right.post_order()
        post_result.append(self.node_id)


sys.setrecursionlimit(10 ** 6)

post_result = []
pre_result = []


def solution(nodeinfo):
    queue = [(x, y, idx + 1) for idx, (x, y) in enumerate(nodeinfo)]
    queue.sort(key=lambda q: q[1], reverse=True)

    root = Node(queue[0][0], queue[0][2])
    queue = queue[1:]

    for x, y, node_id in queue:
        root.insert(x, node_id)
    root.pre_order()
    root.post_order()
    answer = [pre_result, post_result]
    return answer
