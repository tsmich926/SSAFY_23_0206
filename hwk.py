TC = int(input())
# A = [,1,2,3,4,5,6,7,8,9,10,11,12]
A = [i for i in range(1,13)]
for tc in range(1,TC+1):
    N,K =map(int,input().split())
    res = 0
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
    print(res)

