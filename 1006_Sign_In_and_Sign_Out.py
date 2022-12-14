'''

题目

At the beginning of every day, the first person who signs in the computer room will unlock the door, and the last one who signs out will lock the door. Given the records of signing in's and out's, you are supposed to find the ones who have unlocked and locked the door on that day.
Input Specification:

Each input file contains one test case. Each case contains the records for one day. The case starts with a positive integer M, which is the total number of records, followed by M lines, each in the format:
ID_number Sign_in_time Sign_out_time
where times are given in the format HH:MM:SS, and ID_number is a string with no more than 15 characters.
Output Specification:

For each test case, output in one line the ID numbers of the persons who have unlocked and locked the door on that day. The two ID numbers must be separated by one space.
Note: It is guaranteed that the records are consistent. That is, the sign in time must be earlier than the sign out time for each person, and there are no two persons sign in or out at the same moment.
Sample Input:

3
CS301111 15:30:28 17:00:10
SC3021234 08:00:00 11:25:25
CS301133 21:45:00 21:58:40
Sample Output:

SC3021234 CS301133

解题思路

这道题比较简单，主要方法是读入并遍历所有记录的同时，维护最早进入时间和该用户的id 与 最晚离开时间和该用户的id。
比较时间时，可以先将存储时间的 str 用 str.split(':') 分隔成数列，用 list(map(int, list)) 转换成 整型数列，然后转换成统一的秒单位计时，再进行大小比较

'''


n = int(input())

start, end = 24 * 60 * 60 - 1, 0
first_in, last_out = -1, -1
for _ in range(n):
    idx, sign_in, sign_out = list(input().split())
    sign_in = list(map(int, sign_in.split(':')))
    sign_out = list(map(int, sign_out.split(':')))
    sign_in = 3600 * sign_in[0] + 60 * sign_in[1] + sign_in[2]
    sign_out = 3600 * sign_out[0] + 60 * sign_out[1] + sign_out[2]
    if sign_in < start:
        start = sign_in
        first_in = idx
    if sign_out > end:
        end = sign_out
        last_out = idx
print(first_in, last_out)


