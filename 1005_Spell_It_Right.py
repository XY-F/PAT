'''

题目

Given a non-negative integer N, your task is to compute the sum of all the digits of N, and output every digit of the sum in English.
Input Specification:

Each input file contains one test case. Each case occupies one line which contains an N (≤10 
100
 ).
Output Specification:

For each test case, output in one line the digits of the sum in English words. There must be one space between two consecutive words, but no extra space at the end of a line.
Sample Input:

12345
Sample Output:

one five

解题思路

这是比较简单的一题，主要用到的技巧是用str()直接讲整型转换成字符，然后顺序地读取字符并进行转换。
转换后的字符先是放在一个list中，然后用 ' '.join(list) 进行连接，最后输入结果

'''

nums = input()
ans = 0
for i in nums:
    ans += int(i)

ans = str(ans)
res = []
for i in ans:
    if i == '0':
        res.append('zero')
    elif i == '1':
        res.append('one')
    elif i == '2':
        res.append('two')
    elif i == '3':
        res.append('three')
    elif i == '4':
        res.append('four')
    elif i == '5':
        res.append('five')
    elif i == '6':
        res.append('six')
    elif i == '7':
        res.append('seven')
    elif i == '8':
        res.append('eight')
    elif i == '9':
        res.append('nine')
print(' '.join(res))
    
    

