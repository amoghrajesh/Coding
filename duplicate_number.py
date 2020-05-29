#l=list(map(int,input().split()))
#n=len(l)  #5 in this case
#sn=(n)*(n+1)//2 #15
#sl=sum(l) #12
#diff=sn-sl
#return n-diff
#
#
#

nums=list(map(int,input().split()))
hashmap=dict()
for i in nums:
    if i not in hashmap:
        hashmap[i]=1
    else:
        hashmap[i]+=1
for k,v in hashmap.items():
    if v>1:
        return k