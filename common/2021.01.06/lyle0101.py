import sys


def is_vps(ps):

    ps_split = list(ps)
    ps_split.reverse()
    lb_count, rb_count = 0, 0

    while (ps_split):
        item = ps_split.pop()

        if (item == "("):
            lb_count += 1
        else:
            rb_count += 1

        if (rb_count > lb_count):
            return False

    return lb_count == rb_count


if __name__ == "__main__":

    ps_list = []
    ps_num = int(sys.stdin.readline())

    for _ in range(ps_num):
        ps = sys.stdin.readline()
        ps_list.append(ps.strip("\n"))

    for i in ps_list:
        if (is_vps(i)):
            print("YES")
        else:
            print("NO")
