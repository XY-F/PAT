'''

题目

The highest building in our city has only one elevator. A request list is made up with N positive numbers. The numbers denote at which floors the elevator will stop, in specified order. It costs 6 seconds to move the elevator up one floor, and 4 seconds to move down one floor. The elevator will stay for 5 seconds at each stop.
For a given request list, you are to compute the total time spent to fulfill the requests on the list. The elevator is on the 0th floor at the beginning and does not have to return to the ground floor when the requests are fulfilled.
Input Specification:

Each input file contains one test case. Each case contains a positive integer N, followed by N positive numbers. All the numbers in the input are less than 100.
Output Specification:

For each test case, print the total time on a single line.

Sample Input:

3 2 3 1

Sample Output:

41

解题思路

先求出相邻楼层之间的间隔，然后用模拟的方式求出结果

'''


nums = list(map(int, input().split()))[1:]


floors = [nums[0]] + [nums[i] - nums[i - 1] for i in range(1, len(nums))]

#print(floors)
ans = 0
for i in floors:
    if i > 0:
        ans += 6 * i
    else:
        ans -= 4 * i
    ans += 5

print(ans)

