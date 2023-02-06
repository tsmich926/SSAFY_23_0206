A = [1,2,3,4]
bit = [0]*4
for i in range(2):
    bit[0] = i
    for i in range(2):
        bit[1] = i
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit,end=' ')
                for p in range(4):
                    if bit[p]:
                        print(A[p],end=' ')
                print()


arr = [3,6,7,1,5,4]

n = len(arr)
for i in range(1<<n): # 1<<n:부분 집합의 개수 
    for j in range(n): #원소의 수만큼 비트비교
        if i & (i<<j): #i의 j번 비트가 1인경우
            print(arr[j], end=", ") #j번원소출력
    print()
print()

s = ['1','2','3','2']
s[1] = '1' #문자열은 이뮤터블이므로 변경이 안된다. 에러발생
cnt = [0] * 10
for c in s:
    cnt[int(c)] += 1
print(cnt)

m = []*2
m[0] = input()
m[1] = input()
print(m)

m = []
m.append(input())
m.append(input())
print(m)

"12 32 345" = > [12,32,345]
l = map(int,input().split())
"1232" => [1,2,3,2]

#1차원
s= [input() for _ in range(5)]
l= list(map(int,input()))

# 3X4 이차원 배열을 입력
12 34 32
34 45 32
...
...
l = list(map(int,input()))



#4X3 배열을 입력
12 34 32
34 45 32
12 34 32
34 45 32
...

M=4, N=3
l = [list(map(int,input().split())) for _ in range(M)]
#print(l)
#12 34 32 34 45 32
# 행우선
# 0 row
 0 col, 1col, 2col
#1 row
i row에 대해 각 col (0~2)
for i in range(0,M):
    for col in range(0,N-1):
        print(l[i][col])
# 열우선
# 0 col
   0row, 1 row,2row ,3row (M-1)
i col
for i in range(0,N):
    for row in range(0,M):
        print(l[row][i])

#가로의 합 중 가장 큰 값을 구하라
l = [list(map(int,input().split())) for _ in range(M)]

#0 row의 합을 구한다
l[0][0] + l[0][1] + l[0][2]
sumV= 0
for col in range(0,N):
    sumV += l[l][col]

1 row의 합
l[1][0] + l[1][1] +l[1][2]
sumV =0
for col in range(0,N):
    sumV +=l[i][col]

maxV = 0
for row in range(0,M):
    sumV = 0
    for col in range(0,N):
        sumV += l[low][col]
    print(sumV)
    if maxV < sumV:
        maxV = sumV
print(maxV)

#세로의 합 중 가장 큰 값을 구하라


l = [list(map(int,input().split())) for _ in range(M)]
0 col 합
l[0][0] + l[1][0] + l[2][0] + l[3][0]
1 col 합
l[0][1] + l[1][1]+ l[2][1] +l[3][1]
i col 합
l[0][i] + l[1][i]+ l[2][i] +l[3][i]
for i in range(N):
    sumV = 0
    for row in range(M):
        sumV += l[row][i]

for row in range(M):
    sumV = 0
    for col in range(M):
        sumV +=l[row][col]
    print(sumV)
M과 N이 같다면 :
for i in range(N):
    sumR = 0
    sumC = 0
    for j in range(N):
        sumR += l[i][j]
        sumC += l[j][i]

M=4
N=2
for row in range(M):
    sumV = 0
    for col in range(N):
        sumV += l[row][col]
    print(sumV)

TC = int(input())
TC = 1
for tc in range(1,TC+1):
    N =int(input())
    Arr = [list(map(int,input().split())) for _ in range(N)]
    print(Arr)

    for row in range(N):
        for col in range(N):
            print(row,col,Arr[row][col])
로우만 뽑아내면dr =[-1,1,0,0]
dc = [0,0,-1,1]
위로 -1,0
아래:1,0
왼:0,-1
오:0,1
r,c

def my_abs(value):
    if value < 0 :
        return value(*-1)
    return value

sumV = 0
for row in range(N):
    for col in range(N):
        # for d in range(4):
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)] #위 오른 아래 왼
            newR = row+dr
            newC = col+dc
            if 0<=newR <N and 0<=newC<N:
                newValue = Arr[newR][newC]
                sumV += my_abs(Arr[row][col] - Arr[newR][newC])
                
            #if 정상범위가 아니라면
            # continue
            if 0<=newR <N and 0<=newC<N:
                newValue = Arr[newR][newC]
                sumV += my_abs(Arr[row][col] - Arr[newR][newC])
print(tc,sumV)

##부분집합의 총 갯수
#부분집합에 포함되는가?
#{} 
[10,20,30,40]
0000
0001
0010
0011
0110
...
#부분집합의 갯수 16개

arr = [10,20,30]
for i0 in [0,1]:
    for i1 in [0,1]:
        for i2 in [0,1]:
            if i0 == 1:
                print(arr[0],end=' ')
            if i0 == 1:
                print(arr[1],end=' ')
            if i0 == 1:
                print(arr[2],end = ' ')
        print()

print(13,bin(13))

10진수 (0~9)10345:10345 =1*10^4 +0*10^3 ...
2진수 (0~1)1101:1*2^3 + 1*2^3+...
[10,20,30]
000:0
001:1
010:2
011
...
111:7(2^3-1) :1000-1 : 1<<N-1
원소가 N개이면 부분집합의 갯수는 2^N:0~2^N-1

N=3
arr = [10,20,30]
for n in range(0,1<<N):
    print(bin(n))

N = 3 #원소개수 3개 각각 비트수를 표현
n = 5 #101 {10,30}
0 & 1 => 0
1 & 1 => 1
0 & 0 => 0

 101
&001
=====
 001

n=5
for j in range(N):
    r = n&(1<<j)
    if r != 0:
        print(arr[j],end =' ')

n = 3
arr = [10,20,30]
for n in range(0,1<<N):
    for j in range(N):
        r = n&(i<<j)
        if r!= 0:
            print(arr[j],end='')
    print()

#연습문제2 10개의 정수를 입력받아 부분집합의 합이0이 되는것이 존재하는지 계산하는 함수 작성

#색칠하기
     칼라 1
33 66 칼라2
test_case

빈보드판 만들기
TC = int(input())
for tc in range(1,TC+1):
    N =int(input())

    brd = [[0]*10] for _ in range(10):
    brd[1][1] = 3
    print(brd)
    brd = [0] * 10 for _ in range(10)
        for 영역 갯수만큼 입력받아서 =:
            각 영역별로 색을 칠한다.

        #전 영역에 대하여 3의 갯수를 센다.
        for r in range(10):
            for c in range(10):
                if brd[r][c] == 3 :

                    TC = int(input())
                    for tc in range(1, TC + 1):
                        N = int(input())

""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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



#부분합

TC = int(input())
# A = [,1,2,3,4,5,6,7,8,9,10,11,12]
A = [i for i in range(1,13)]
    for tc in range(1,TC+1):
        N,K =map(int,input().split())
        for n in range(1<<12):
            #n에 대하여 이진수 출력
            cnt = 0
            sumV = 0
            for j in range(12):
                r = n&(1<<j)
                if r != 0:
                    cnt += 1
                    sumV += A[j]
                    #부분집합에 포함
            if cnt == N and sumV == K:
                res += 1


sumV = 0
for row in range(N):
    sumV += arr[row][row]

sumV = 0
for row in range(N):
    sumV += arr[row][99-row]








