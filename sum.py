# arr = [3,4,7,1,5]
# n =len(arr)
# for i in range(1<<n):
#     for j in range(n):
#         if i & (i<<j):
#             print(arr[j],end=' , ')
#     print()

arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

# 모든 부분집합을 저장할 리스트
subset_list = []

# 이진수와 비트연산자를 활용
for i in range(1 << n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])
    subset_list.append(subset)

print(subset_list)



T = int(input())
set_list = [ i for i in range(1, 13)]
m = len(set_list)

for case in range(1, T+1):
    n, k = map(int,input().split())
    ans = 0
    for i in range(1<<m):
        cnt = 0
        sum = 0
        for j in range(m):
            if i & (1<<j):
                sum += set_list[j]
                cnt += 1
        if cnt == n and sum == k:
            ans += 1
    print('#{} {}'.format(case, ans))