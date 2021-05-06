# MiniCost-Knapsack-Algo


- use dynamic programming approch
- data is given in a file
- frist line of the file is used to give no of values```NoOfValues <No of values given>```
- Following lines consists of weight value pair ```<weight> <value>```
- Exaple data.txt file

```

NoOfValues 3
10 60
20 100
30 120

```

## Run the programme
```
python MiniCostKnapsack.py <name of the data file>

```

- Optimized knapsak problem with FPATS consists of FPTASKnapsack.py
1. Find the maximum valued item,find maximum value in value array. Let this maximum value be maxVal.
2. Compute adjustment factor k for all values
3. Adjust all values, i.e., create a new array valFptas that values divided by k. Do following for every value value[i].
4. Run ``` MaximumKnapsack(value: list,cost: list) ``` on valFptas array and cost array

```
k  = (maxVal * ε) / n

valFptas[i] = floor(val[i] / k)

```

## Run the programme
```
python FPTASKnapsack.py <name of the data file>

```