#2차원배열
N =int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
print(arr)

# 3
# 1 2 3
# 4 5 6
# 7 8 9
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#배열순회
for i in range(n):
    for j in range(m):
        Array[i][j]

#열 우선순회
for j in range(m):
    for i in range(n):
        Array[i][j]

#지그재그
for i in range(n):
    for j in range(m):
        Array[i][j + (m-1-2*j) * (i%2)]

#델타를 이용한 2차배열 탐색
di = [0,1,0,-1]
dj = [1,0,-1,0]
N=3
p=3
for i in range(N):
    for j in range(N):
        for k in range(4):
            for l in range(1,p+1)
                ni, nj = i_di[k], j+dj[k]
                if 0 <= ni <N and 0<=nj<N:
                    print(i,j,ni,nj)
N = 3
for i in range(N):
    for j in range(N):
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i+di, j+dj
            if 0<= ni<N and 0<=nj<N:
                print(i,j,ni,nj)

#전치행렬
arr = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(3):
        if i < j :
            arr[i][j], arr[j][i] = arr[j][i],arr[i][j]

#부분집합 생성
#부분집합에 포함되지 않으면 0,포함되면 1
#부분집합에 대한 포함여부를 판단하는 배열을 생성
bit = [0,0,0,0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
A = [1,2,3,4]
bit = [0]*4
for i in range(2):
    bit[0] = i
    for k in range(2):
        bit[2] = k
        for l in range(2):
            bit[3] = l
            print(bit)