‘’‘ 

题目
As an emergency rescue team leader of a city, you are given a special map of your country. The map shows several scattered cities connected by some roads. Amount of rescue teams in each city and the length of each road between any pair of cities are marked on the map. When there is an emergency call to you from some other city, your job is to lead your men to the place as quickly as possible, and at the mean time, call up as many hands on the way as possible.
Input Specification:

Each input file contains one test case. For each test case, the first line contains 4 positive integers: N (≤500) - the number of cities (and the cities are numbered from 0 to N−1),
M - the number of roads,and C1 -  C2 the cities that you are currently in and that you must save, respectively. The next line contains N integers, 
where the i-th integer is the number of rescue teams in the i-th city. Then M lines follow, each describes a road with three integers 
Each input file contains one test case. For each test case, the first line contains 4 positive integers: N (≤500) - the number of cities (and the cities are numbered from 0 to N−1),
M - the number of roads,and  - the cities that you are currently in and that you must save, respectively. The next line contains N integers, where the i-th integer is the number of rescue teams in the i-th city. 
Then M lines follow, each describes a road ith three integers c1, c2 and L, which are the pair of cities connected by a road and the length of that road, respectively. 
It is guaranteed that there exists at least one path from C1 to C2.

Output Specification:

For each test case, print in one line two numbers: the number of different shortest paths between C1 and  C2 the maximum amount of rescue teams you can possibly gather. 
All the numbers in a line must be separated by exactly one space, and there is no extra space allowed at the end of a line.

Sample Input:

5 6 0 2
1 2 1 5 3
0 1 1
0 2 2
0 3 1
1 2 1
2 4 1
3 4 1

Sample Output:

2 4

代码长度限制
16 KB
时间限制
400 ms
内存限制
64 MB

解题思路：主要运用 dijkstra 求解单源最短路径，利用 path_num， path_max_hands 记录经 过指定节点的最短路径数量 和 可以召唤的最大帮手人数。
运用 first_round 变量使得循环适用于只存在一个城市的情况，用python提供的 set变量 unvisited_cities 来标记未处理过的城市，避免多余的循环判断

本人踩过的坑：在生成 graph 时注意城市之间构成的是无向图，需要在邻接矩阵中添加两条边，否则测例无法通过

’‘’

cities_num, roads, start, end = list(map(int, input().split()))
cities = set([i for i in range(cities_num)])
hands = list(map(int, input().split()))
graph = [[float('inf')] * cities_num for _ in range(cities_num)] 

for i in range(cities_num):
    graph[i][i] = 0

while True:
    try:
        row, column, length = list(map(int, input().split()))
        graph[row][column] = length
        graph[column][row] = length
    except:
        break

distance = [i for i in graph[start]]
path_max_hands = [i for i in hands]
path_num = [0 for _ in range(cities_num)]
path_num[start] = 1
unvisited_cities = cities - set([start])

first_round = True
while True:
    if first_round:
        target_city = start
        first_round = False
        
    else:
        target_city = -1
        min_distance = float('inf')
        for next_city in unvisited_cities:
            if distance[next_city] < min_distance:
                min_distance = distance[next_city]
                target_city = next_city
        if min_distance == float('inf') or not unvisited_cities:
            print(path_num[end], path_max_hands[end])
            break            
    unvisited_cities -= set([target_city])
    for next_city in unvisited_cities:
        temp_distance = distance[target_city] + graph[target_city][next_city]
        temp_hands = path_max_hands[target_city] + hands[next_city]
        if temp_distance < distance[next_city]:
            distance[next_city] = temp_distance
            path_num[next_city] = path_num[target_city]
            path_max_hands[next_city] = temp_hands
        elif temp_distance == distance[next_city]:
            path_num[next_city] += path_num[target_city]
            path_max_hands[next_city] = max(temp_hands, path_max_hands[next_city])
    
            
