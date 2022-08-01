'''

题目

To evaluate the performance of our first year CS majored students, we consider their grades of three courses only: C - C Programming Language, M - Mathematics (Calculus or Linear Algrbra), and E - English. At the mean time, we encourage students by emphasizing on their best ranks -- that is, among the four ranks with respect to the three courses and the average grade, we print the best rank for each student.

For example, The grades of C, M, E and A - Average of 4 students are given as the following:

StudentID  C  M  E  A
310101     98 85 88 90
310102     70 95 88 84
310103     82 87 94 88
310104     91 91 91 91

Then the best ranks for all the students are No.1 since the 1st one has done the best in C Programming Language, while the 2nd one in Mathematics, the 3rd one in English, and the last one in average.

Input Specification:

Each input file contains one test case. Each case starts with a line containing 2 numbers N and M (≤2000), which are the total number of students, and the number of students who would check their ranks, respectively. Then N lines follow, each contains a student ID which is a string of 6 digits, followed by the three integer grades (in the range of [0, 100]) of that student in the order of C, M and E. Then there are M lines, each containing a student ID.

Output Specification:

For each of the M students, print in one line the best rank for him/her, and the symbol of the corresponding rank, separated by a space.

The priorities of the ranking methods are ordered as A > C > M > E. Hence if there are two or more ways for a student to obtain the same best rank, output the one with the highest priority.

If a student is not on the grading list, simply output N/A.

Sample Input:

5 6
310101 98 85 88
310102 70 95 88
310103 82 87 94
310104 91 91 91
310105 85 90 90
310101
310102
310103
310104
310105
999999

Sample Output:

1 C
1 M
1 E
1 A
3 A
N/A

解题思路

读入学生成绩信息，分别依据四个项目进行排序，设置一个 dict() 以学生 id 为 key 记录学生在四个项目的排名，在输出阶段，计算、搜索、输出一个学生的最高排名科目。

踩坑提示

对于成绩相同的情况排名相同，但是注意下面这个例子： 排名应该 1 1 3 4 而不是 1 1 2 4，也就是排名可以相同，但是重复的排名要计数。
对此，我的解决方法是遍历的时候，当遇到分数相同的情况，排名不变，分数不同时，排名计数 a = i + 1.
如果不做这些处理，无法通过测试点 2.

'''

num_student, num_res = list(map(int, input().split()))

record = list()
student_grade = dict()
for i in range(num_student):
    idx, c, m, e = list(map(int, input().split()))
    record.append((idx, (c + m + e) / 3, c, m, e))

A = sorted(record, key = lambda x:x[1], reverse=True)
C = sorted(record, key = lambda x:x[2], reverse=True)
M = sorted(record, key = lambda x:x[3], reverse=True)
E = sorted(record, key = lambda x:x[4], reverse=True)

last_A = last_C = last_M = last_E  = float('inf')
for i in range(len(A)):
    temp_A = A[i][1]
    if temp_A < last_A:
        a = i + 1
    try: 
        student_grade[A[i][0]][0] = a
    except:
        student_grade[A[i][0]] = [a, -1, -1, -1]
    last_A = temp_A
    
    temp_C = C[i][2]
    if temp_C < last_C:
        c = i + 1
    try: 
        student_grade[C[i][0]][1] = c
    except:
        student_grade[C[i][0]] = [-1, c, -1, -1]
    last_C = temp_C
    
    temp_M = M[i][3]
    if temp_M < last_M:
        m = i + 1
    try: 
        student_grade[M[i][0]][2] = m
    except:
        student_grade[M[i][0]] = [-1, -1, m, -1]
    last_M = temp_M
    
    temp_E = E[i][4]
    if temp_E < last_E:
        e = i + 1
    try: 
        student_grade[E[i][0]][3] = e
    except:
        student_grade[E[i][0]] = [-1, -1, -1, e]
    last_E = temp_E

item = ['A', 'C', 'M', 'E']
for  _ in range(num_res):
    idx = int(input())
    try:
        highest_rank = min(student_grade[idx])
        for i in range(4):
            if student_grade[idx][i] == highest_rank:
                print(str(highest_rank), item[i])
                break
    except:
        print('N/A')
    
        
