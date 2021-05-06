from MiniCostKnapsack import MaximumKnapsack
import sys
import time
import math

def FptasMaximumKnapsack(value: list,cost: list,z: float):
    maxVal=max(value)
    k=(maxVal * z) / len(value)
    valFptas=[]
    for val in value:
        valFptas.append(math.floor(val / k))
    
    return MaximumKnapsack(valFptas,cost)
        
    

    


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
            mincost,take=FptasMaximumKnapsack(valuue,cost,0.5)
            seconds = seconds-time.time()
            print('Answer to Min cost FPTAS optimized Knapsack problem :')
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
        print('Invalid no of Arguments :: python FPTASKnapsack.py.py <filename> ')