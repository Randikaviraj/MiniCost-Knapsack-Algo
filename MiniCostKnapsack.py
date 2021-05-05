import sys
import time


def MaximumKnapsack(value: list,cost: list):
    amax=0
    for i in range(len(value)):
        if value[i]>value[amax]:
            amax=i
    Mincost=[ [0] * ((len(value)*value[amax])+1) for _ in range(len(value))]
    Take=[ [0] * ((len(value)*value[amax])+1) for _ in range(len(value))]

    for i in range(len(value)):
        Mincost[i][0]=0
        
    for t in range(1,value[0]+1):
        Mincost[0][t]=cost[0]
        Take[0][t]="YES"
        
    for t in range((value[0]+1),((len(value)*value[amax])+1)):
        Mincost[0][t]=float('inf')
        Take[0][t]="NO"
        
    for i in range(1,len(value)):
        for t in range(1,((len(value)*value[amax])+1)):
            NextT=max(0,t-value[i])
            if Mincost[i-1][t]<=(cost[i]+Mincost[i-1][NextT]):
                Mincost[i][t]=Mincost[i-1][t]
                Take[i][t]="No"
            else:
                Mincost[i][t]=cost[i]+Mincost[i-1][NextT]
                Take[i][t]="Yes"
    return (Mincost,Take)
    


if __name__ =="__main__":
    try:
                
        with open(sys.argv[1],"r") as file:
            print(f"{sys.argv[1]} Reading..")
            line=file.readline()
            noOfValues=int(line.split(" ")[1])
            cost=[]
            valuue=[]
            line=file.readline()
            while line:
                list=line.split(" ")
                costValuePair=[]       
                for item in list:
                    item=item.strip('\n')
                    if item:
                        costValuePair.append(int(item))
                valuue.append(costValuePair[0])
                cost.append(costValuePair[1])
                line=file.readline()

            print('Algorithm Started::')
            seconds = time.time()
            mincost,take=MaximumKnapsack(valuue,cost)
            seconds = seconds-time.time()
            print('Answer to Min cost Knapsack problem :')
            print("____________________________________________________________________________")
            for i in mincost :
                print(i)
            for i in take:
                print(i)
            print("____________________________________________________________________________")
            print('Finished::')
            print('Running Time in second'+str(seconds))
            
    except Exception as e:
        print(e)
        print('Invalid no of Arguments :: python MiniCostKnapsack.py <filename> ')