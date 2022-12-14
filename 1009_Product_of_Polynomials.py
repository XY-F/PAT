‘’‘

题目

This time, you are supposed to find A×B where A and B are two polynomials.
Input Specification:

Each input file contains one test case. Each case occupies 2 lines, and each line contains the information of a polynomial:
$ K N_1 a_N_1 N_2 a_N_2 ... N_K a_N_K $

where K is the number of nonzero terms in the polynomial,	N_i and a_N_i (i=1,2,⋯,K) are the exponents and coefficients, respectively.
It is given that 1 ≤ K ≤ 10, 0 ≤ N_K < ... < N_2 < N_1 ≤ 1000.

Output Specification:

For each test case you should output the product of A and B in one line, with the same format as the input. Notice that there must be
NO extra space at the end of each line. Please be accurate up to 1 decimal place.

Sample Input:

2 1 2.4 0 3.2
2 2 1.5 1 0.5

Sample Output:

3 3 3.6 2 6.0 1 1.6

解题思路

多项式乘法是每一项系数相乘，指数相加，需要两重循环交叉处理。可以用 python 的 dict 创建一个 hash 表来记录指数相同的项的系数大小。
最后将 dict 的 keys 用 sorted 转换成有序的 list，依序对结果进行遍历输出。

踩坑提示

在遍历 dict 的时候注意判断 系数 是否为 零，我一开始把系数为零的判断只写在了生成 dict 的过程中，是不对/不完全的，因为项之间两两相乘之后系数可能会抵消。
如果不做这个判断，见无法通过 测试点 0 。

’‘’

n1 = list(map(float, input().split()))[1:]
n2 = list(map(float, input().split()))[1:]
 
hashtable = dict()
for i in range(0, len(n1), 2):
    for j in range(0, len(n2), 2):
        temp = round(n1[i + 1] * n2[j + 1], 1)
        if temp != 0:
            try:
                hashtable[int(n1[i] + n2[j])] += temp
            except:
                hashtable[int(n1[i] + n2[j])] = temp

keys = sorted(list(hashtable.keys()), reverse=True)

ans = []
for i in keys:
    if hashtable[i] != 0:
        ans += [str(i)]
        ans += [str(hashtable[i])]
    else:
        hashtable.pop(i)
print(' '.join([str(len(hashtable))] + ans))
    

    

