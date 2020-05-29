t=int(input())
for i in range(t):
    s=input()
    s1=s.lower()
    if(s1=='b'):
        print("BattleShip")
    elif(s1=='c'):
        print("Cruiser")
    elif(s1=='d'):
        print("Destroyer")
    elif(s1=='f'):
        print("Frigate")
