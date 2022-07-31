'''

Given a pair of positive integers, for example, 6 and 110, can this equation 6 = 110 be true? The answer is yes, if 6 is a decimal number and 110 is a binary number.

Now for any pair of positive integers N1 and N2, your task is to find the radix of one number while that of the other is given.

Input Specification:

Each input file contains one test case. Each case occupies a line which contains 4 positive integers:

N1 N2 tag radix

Here N1 and N2 each has no more than 10 digits. A digit is less than its radix and is chosen from the set { 0-9, a-z } where 0-9 represent the decimal numbers 0-9, and a-z represent the decimal numbers 10-35. The last number radix is the radix of N1 if tag is 1, or of N2 if tag is 2.

Output Specification:

For each test case, print in one line the radix of the other number so that the equation N1 = N2 is true. If the equation is impossible, print Impossible. If the solution is not unique, output the smallest possible radix.

Sample Input 1:

6 110 1 10

Sample Output 1:

2

Sample Input 2:

1 ab 1 2

Sample Output 2:

Impossible

解题思路

将 N1 和 N2 都转换成 十进制数 进行比较，为此需要 编写一个 decimal_digit() 函数，再通过二分查找的方式，对有序的可能的 基数 进行查找比较。

踩坑提示

1. 题目要求 当存在多种满足条件的 基数 时，输出最小的那个。达到这一目的的最简单方法是将 二分查找 的范围设置成 (0, n1 + 1), 也可以设置成 (2, n1 + 1), 因为最小的基数是 2。  
2. 将 数 转换成 十进制数 时，注意判断当前位的 数 是否大于基数，如果大于基数，则返回 -1， 在二分查找中，对这种情况按照 left = mid + 1 处理。
3. 二分查找的边界曾经困扰我很长一段时间，现在我一般常用的写法是 while left <= right, 在循环中 加上 if left > right: 的判断。目前为止这种写法都能顺利解决问题。

'''

def decimal_digit(num, radix):
    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    n = 0
    num = num[::-1]
    for i in range(len(num)):
        if num[i] not in digits:
            temp = (ord(num[i]) - ord('a') + 10)
            if temp < radix:
                n += temp * radix ** i
            else:
                return -1
        else:
            if int(num[i]) < radix:
                n += int(num[i]) * radix ** i
            else:
                return -1
    return n


def find_radix(n1, n2, n1_radix):
    # 默认 n1 是十进制数
    left, right = 0, n1 + 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        temp = decimal_digit(n2, mid)
        if temp == -1:
            left = mid + 1
        elif temp == n1:
            return mid
        elif temp < n1:
            left = mid + 1
        elif temp > n1:
            right = mid - 1
        if left > right:
            mid = (left + right) // 2
            temp = decimal_digit(n2, mid) 
            if temp == n1:
                return mid
    return -1
    
N1, N2, tag, radix = input().split()
radix = int(radix)

if tag == '1':
    N1 = decimal_digit(N1, radix)
    res = find_radix(N1, N2, radix)
elif tag == '2':
    N2 = decimal_digit(N2, radix)
    res = find_radix(N2, N1, radix)

if res == -1:
    print('Impossible')
else:
    print(res)

    

    
   
