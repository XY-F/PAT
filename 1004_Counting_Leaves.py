‘’‘

题目

A family hierarchy is usually presented by a pedigree tree. Your job is to count those family members who have no child.
Input Specification:

Each input file contains one test case. Each case starts with a line containing 0<N<100, the number of nodes in a tree, and M (<N), the number of non-leaf nodes. Then M lines follow, each in the format:
ID K ID[1] ID[2] ... ID[K]
where ID is a two-digit number representing a given non-leaf node, K is the number of its children, followed by a sequence of two-digit ID's of its children. For the sake of simplicity, let us fix the root ID to be 01.
The input ends with N being 0. That case must NOT be processed.
Output Specification:

For each test case, you are supposed to count those family members who have no child for every seniority level starting from the root. The numbers must be printed in a line, separated by a space, and there must be no extra space at the end of each line.
The sample case represents a tree with only 2 nodes, where 01 is the root and 02 is its only child. Hence on the root 01 level, there is 0 leaf node; and on the next level, there is 1 leaf node. Then we should output 0 1 in a line.

Sample Input:

2 1
01 1 02

Sample Output:

0 1

解题思路

从输入信息中生成一个树，然后从根节点用一个队列层序遍历这棵树，记录每一层的叶子结点数量并输出。
判断层次时用到了 curr_level 和 last_level，level值是在遍历时和节点一起存储到队列中，用队列中弹出节点时，level值发生变化说明遍历到了新的一层

踩坑提示
当树只有一个根节点时需要单独判断

Input:
1 0

Output:
1

‘’‘

import collections


class TNode:
    def __init__(self, c=None, b=None):
        self.child = c
        self.brother = b
 
        
num_nodes, num_nonleaf = list(map(int, input().split()))
table_nodes = dict()

while True:
    try:
        info = list(map(int, input().split()))
        try:
            parent = table_nodes[info[0]]
        except:
            parent = TNode()
            table_nodes[info[0]] = parent
        child = info[2:]
        work_node = parent
        first_round = True
        for i in child:
            try:    
                temp_node = table_nodes[i]
            except:
                temp_node = TNode()
                table_nodes[i] = temp_node
            if first_round:
                work_node.child = temp_node
                first_round = False
            else:
                work_node.brother = temp_node
            work_node = temp_node
    except:
        break
        
if len(table_nodes) == 0:
    print('1')
else:
    curr_level = 0
    last_level = 0
    leaf = 0
    # 层序遍历
    root = table_nodes[1]
    q = collections.deque([(root, curr_level)])
    while q:
        last_level = curr_level
        work_node, curr_level = q.popleft()
        if curr_level != last_level:
            print(leaf, end=' ')
            leaf = 0
        if not work_node.child:
            leaf += 1
        else:
            q.append((work_node.child, curr_level + 1))
        while True:
            try:
                work_node = work_node.brother
                if not work_node.child:
                    leaf += 1
                else:
                    q.append((work_node.child, curr_level + 1))
            except:
                break
    print(leaf)







