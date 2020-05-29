'''def anyeven(l):
    for i in l:
        if i%2==0:
            return True
    return False

def allodd(l):
    for i in l:
        if i%2==0:
            return False
    return True

from itertools import combinations
l=[2,4,6,8]
power=set(l)
allsub=[]
for i in range(1,len(l)):
    c=list(combinations(l,i))
    for j in c:
        allsub.append(j)
ans=0
for i in allsub:
    s=set(i)
    left=power-s
    if anyeven(i) and allodd(left):
        ans+=1
print(2*ans)'''


''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
def anyeven(l):
    for i in l:
        if i%2==0:
            return True
    return False

def allodd(l):
    for i in l:
        if i%2==0:
            return False
    return True

from itertools import combinations

def main():

    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        power=set(l)
        allsub=[]
        for i in range(1,len(l)):
            c=list(combinations(l,i))
            for j in c:
                allsub.append(j)
        ans=0
        for i in allsub:
            s=set(i)
            left=power-s
            if anyeven(i) and allodd(left):
                ans+=1
        print(2*ans)



main()


    
