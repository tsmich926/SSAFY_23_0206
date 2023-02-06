Test_case=int(input())

for t in range(1,Test_case+1):
    area=[[0 for _ in range(10)] for _ in range(10)] #원소가 0인 10x10행렬 만들기
    count=0 #겹치는 칸의 개수
    N=int(input())

    for i in range(1,N+1):
        row1,col1,row2,col2,color=map(int,input().split())

        for row in range(row1,row2+1): #행의 시작과 끝까지
            for col in range(col1,col2+1):
                if color==1: #만약 색이 빨간색이면
                    if area[row][col]==0: #만약 색이 아무것도 없는 빈칸이면
                        area[row][col]=1 #빨간색으로 칠하고

                    elif area[row][col]==2: #만약 색이 파란색이면
                        area[row][col]=3 #파란색을 보라색으로 칠해라.
                        count+=1 #그런다음 겹치는 칸의 개수를 세어주기 위해 +1을 해준다.

                else: #만약 색이 파란색이면
                    if area[row][col]==0: #만약 색이 아무것도 없는 빈칸이면
                        area[row][col]=2 #파란색으로 칠해라.

                    elif area[row][col]==1: #만약 색이 빨간색이면
                        area[row][col]=3 #빨간색을 보라색으로 칠해라.
                        count+=1 #그런다음 겹치는 칸의 개수를 세어주기 위해 +1을 해준다.


    print("#{} {}".format(t,count))