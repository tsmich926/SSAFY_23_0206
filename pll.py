# m = []
# m.append(input())
# m.append(input())
# print(m)
#
# "12 32 345" = > [12,32,345]
# l = map(int,input().split())
# "1232" => [1,2,3,2]
#
# #1차원
# s= [input() for _ in range(5)]
# l= list(map(int,input()))

# TC = int(input())
# TC = 1
# for tc in range(1,TC+1):
#     N =int(input())
#     Arr = [list(map(int,input().split())) for _ in range(N)]
#     print(Arr)
#
#     for row in range(N):
#         for col in range(N):
#             print(row,col,Arr[row][col])

# nums = range(1,6)
# idx = len(nums)
# for i in range(1<<idx):
#     temp = []
#     for j in range(idx):
#         if i & (i<<j):
#             temp.append(nums[j])
#     if sum(temp) == 10:
#         print(*temp)

#1에서 5까지의 부분집합
#idx 00000
# nums = range(1,6)
# idx = len(nums)
# for i in range(1 << idx):
#     temp = []
#     for j in range(idx):
#         if i & (1<<j):
#             temp.append(nums[j])
#     print(temp)

TC = int(input())
for tc in range(1,TC+1):
    N =int(input())
    brd = [[0]*10 for _ in range(10)]
    for _ in range(N):
        r1,c1,r2,c2,color =map(int,input().split())
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                brd[r][c] += color

    res = 0
    for r in range(10):
        for c in range(10):
            if brd[r][c] == 3:
                res += 1
    print(res)


행순회
sumV = 0
for i in range(n):
    for j in range(m):
        sumV += array[i][j]
열순회
for j in range(m):
    for i in rnage(n):
        sumv += array[i][j]
지그재그 순회