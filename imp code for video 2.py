a=input("enter the word")   
b=""                                         
for i in a:                                     
    b=b+i
    print(b)

#######################################################################3
a=50 # or  a=int(input()) if it  is a user input question
print("#"*a,end="\n") #its the first line of pattern
i=(a//2)-1
j=2
while(i!=0):
    while(j<=(a-2)):
        print("#"*i,end="")
        print("_"*j,end="")
        print("#"*i,end="\n")
        i=i-1
        j=j+2
###############################################################
for i in range(0,6):
    for j in range(5,i,-1):
        print(j,'',end='')
    for l in range(i):
        print('',end='')
    for k in range(i+1,6):
        print(k,'',end='')
    print('\n')
#################################
    print("Enter limit: ")
n = int(input())
i  = 1
while(i <= n):
    j = 1
    while (j = j):
        print(format(i, "2d"), end=' ')
    else:
        print(format(j, "2d"), end=' ')
        j = j + 1
    print()
    i = i + 1
######################################
    num=int(input('Enter a number: '))

while num<=0:
    print('Error! Enter a positive number: ')
    num=int(input('Enter a number: '))
for row in range (num):
    for col in range (row):
        print('*', end='')
    print()
for i in range (num,0,-1):
    for j in range (i):
        print('*', end='')
    print()
    ########################################
N = int(5)
M = int(5)
for i in range(1,N,2):
    print((i * ".|.").center(M, "-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2):
    print((i * ".|.").center(M, "-"))
