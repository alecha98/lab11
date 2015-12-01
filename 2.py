from Point import*
N=int(input())-1
max=Point(input())
for i in range (N):
    a=Point(input())
    if a>max:
        max=a
print (max)
