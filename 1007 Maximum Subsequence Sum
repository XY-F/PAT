‘’‘

题目

Given a sequence of K integers { N1​, N2​, ..., NK​ }. A continuous subsequence is defined to be { Ni​, Ni+1​, ..., Nj​ } where 1≤i≤j≤K. The Maximum Subsequence is the continuous subsequence which has the largest sum of its elements. For example, given sequence { -2, 11, -4, 13, -5, -2 }, its maximum subsequence is { 11, -4, 13 } with the largest sum being 20.

Now you are supposed to find the largest sum, together with the first and the last numbers of the maximum subsequence.

Input Specification:

Each input file contains one test case. Each case occupies two lines. The first line contains a positive integer K (≤10000). The second line contains K numbers, separated by a space.

Output Specification:

For each test case, output in one line the largest sum, together with the first and the last numbers of the maximum subsequence. The numbers must be separated by one space, but there must be no extra space at the end of a line. In case that the maximum subsequence is not unique, output the one with the smallest indices i and j (as shown by the sample case). If all the K numbers are negative, then its maximum sum is defined to be 0, and you are supposed to output the first and the last numbers of the whole sequence.

Sample Input:

10
-10 1 2 3 4 -5 -23 3 7 -21

Sample Output:

10 1 4

解决思路

运用动态规划，可以设置一个和数列 nums 同样长度的 sub_sum_arr, 第[i]项 记录截至 nums[i] 的最大子数列和，sub_sum_arr[i] 的值依据 max_sub_sum[i - 1] + nums[i] 和 nums[i] 大小比较来决定，选择 sub_sum_arr[i] = sub_sum_arr[i - 1] + nums[i] 意味着扩充延伸之前的子数列， 选择 sub_sum_arr[i] = nums[i] 意味着重新开始计数具有最大和的子数列。由于一次顺序的遍历就可以求出全部 sub_sum_arr 而且 不需要输出 sub_sum_arr 的全部信息，可以用 sub_sum 表示 sub_sum_arr[i]， max_sub_sum 记录最大子序列和，用 start_idx 和 end_idx 记录 该序列的起点和终点，可以将空间复杂度降低到 O(1)。

’‘’

while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        sub_sum = nums[0]
        max_sub_sum = nums[0]
        sub_start_idx = 0
        start_idx = 0
        end_idx = 0
        if nums[0] < 0:
            flg = True
        else:
            flg = False
        for i in range(1, n):
            if flg:
                if nums[i] >= 0:
                    flg = False
            temp = sub_sum + nums[i]
            if temp < nums[i]:
                sub_sum = nums[i]
                sub_start_idx = i
            else:
                sub_sum = temp
            if sub_sum > max_sub_sum:
                max_sub_sum = sub_sum
                start_idx = sub_start_idx
                end_idx = i
        if flg:
            print('0', nums[0], nums[-1])
        else:
            print(max_sub_sum, nums[start_idx], nums[end_idx], end='')
    except:
        break
