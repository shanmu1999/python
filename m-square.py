x1,y1=input().split()
x1,y1=int(x1),int(y1)
x2,y2=input().split()
x2,y2=int(x2),int(y2)
yy=y1*2
x3,y3=input().split()
x3,y3=int(x3),int(y3)
xx=x1*2
x4,y4=input().split()
x4,y4=int(x4),int(y4)

if(x1==x2 and yy==y2 and x3==xx and y3==yy and x4==x3 and y4==y1):
    print("yes")
else:
    print("no")
