# omok,  a  game  of paduk with five checkers placed in a row.
# computer network team, 10
# 160513 ver1. no rule , play game

# player 는 1과 2 교대로 1=0, 2=1
# player가 두는 돌은 0->player 번호로 맵핑
#init
def display():    # 판을 보여줌 13x13
    for i in range(13):
        for j in range(13):
            print(locate[i][j],end=" ")
        print()
def isSize(n): # 놓은 위치가 맞는지 확인
    if(1 <= n and n <= 13 and int==type(n)):
        #판안에 존재하며 타입은 인트형이라면
        return True
    return False
def isEmpty(row,col):
    if(locate[row-1][col-1]>2): return True # 플레이어 돌은 0과 1 이므로 2보다크면빈자리
    return False

class queue:
    lst=[]
    def __init__(self):
        self.lst=[]
    def __init__(self,x,y):
        self.lst=[]
        self.lst.append([x,y])
    def push(self, row,col):
        self.lst.insert(0,[row,col])
    def pop(self):
        
        a,b=self.lst.pop()
        return a,b
    def isEmpty(self):
        if(len(self.lst)==0):return True
        return False
        
#구현 check win
def checkWin(P,row,col):# P:Player
    
    QXX=queue(row,col)#-
    QXY=queue(row,col)#\
    QYX=queue(row,col)#/
    QYY=queue(row,col)#|
    print(QXX.lst)
    
    cnt=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QXX.isEmpty()):#-        
        ROW,COL=QXX.pop()        
        cnt+=1
        print("XX",cnt)
        if(locate[ROW][COL-1]==P and visit[ROW][COL-1]==0 and COL-1>=0): visit[ROW][COL-1]=1;QXX.push(ROW,COL-1)
        if(locate[ROW][COL+1]==P and visit[ROW][COL+1]==0 and COL+1<=12):visit[ROW][COL+1]=1;QXX.push(ROW,COL+1)
    if(cnt==5): return True
    
    cnt=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QXY.isEmpty()):#\
        ROW,COL=QXY.pop()
        cnt+=1
        print("XY",cnt,QXY.lst,ROW,COL)
        if(locate[ROW-1][COL-1]==P and visit[ROW-1][COL-1]==0 and ROW-1>= 0 and COL-1>=0): visit[ROW-1][COL-1]=1;QXY.push(ROW-1,COL-1)
        if(locate[ROW+1][COL+1]==P and visit[ROW+1][COL+1]==0 and ROW+1<= 12 and COL+1<=12): visit[ROW+1][COL+1]=1;QXY.push(ROW+1,COL+1)
    if(cnt==5): return True

    cnt=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QYX.isEmpty()):#/
        ROW,COL=QYX.pop()
        cnt+=1
        print("YX",cnt)
        if(locate[ROW-1][COL+1]==P and visit[ROW-1][COL+1]==0 and ROW-1>=0 and COL+1 <= 12): visit[ROW-1][COL+1]=1;QYX.push(ROW-1,COL+1)
        if(locate[ROW+1][COL-1]==P and visit[ROW+1][COL-1]==0 and ROW+1<=12 and COL-1 >= 0): visit[ROW+1][COL-1]=1;QYX.push(ROW+1,COL-1)
    if(cnt==5): return True

    cnt=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QYY.isEmpty()):#|
        ROW,COL=QYY.pop()
        cnt+=1
        print("YY",cnt)
        if(locate[ROW-1][COL]==P and visit[ROW-1][COL]==0 and ROW-1>=0): visit[ROW-1][COL]=1; QYY.push(ROW-1,COL)
        if(locate[ROW+1][COL]==P and visit[ROW+1][COL]==0 and ROW+1<=12):visit[ROW+1][COL]=1; QYY.push(ROW+1,COL)
    if(cnt==5): return True

    return False
# 미구현
##def checkRule(P,row,col):

locate=[[5 for i in range(13)] for j in range(13)] # 판 초기화
#플레이어 이름은 리스트로 이름, 돌번호 로 매핑 시킬 수 있기때문에 나중에 작업.
player=0    
row,col=-1,-1 # init input row col
Winner=False # 승리를 판별 boolean
running=True

while running :
    error=True
    display()
    if(player==0):
        while(error):
            try:
                row,col=(input("돌을 놓을 자리를 입력 (행 열) : ").split())
                row=int(row); col=int(col)
                print(isSize(row),isSize(col))
                if(isSize(row) and isSize(col) and isEmpty(row,col)): error=False;
                else: print("already",row,col)
            except:
                print("Player 1 input error")
            
    elif(player==1):
        while(error):
            try:
                row,col=(input("돌을 놓을 자리를 입력 (행 열) : ").split())
                row=int(row); col=int(col)
                if(isSize(row) and isSize(col) and isEmpty(row,col)): error=False;
                else: print("already",row,col)
            except:
                print("Player 2 input error")
    
    locate[row-1][col-1]=player # 위치에 돌을 놓는다
    Winner=checkWin(player,row-1,col-1)
    if(Winner): #어떤 플레이어가 승리했을 시 
        print(player,'is Winner');
        while True:
            if(int(input("continue play game? 1=y"))==1): break
            else:
                if(int(input("진짜끝냄? 그럼 1 입력해"))==1): running=False;break
    else:
        player=(player+1)%2 # next player

print("Omok is Terminated...")

