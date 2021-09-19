
def knapsack(weights,values,maxWeight):
	table = []
	selected =[]
	for x in range(maxWeight+1):
		table.append(0)
		selected.append([])

	for i in range(maxWeight+1):
		for j in range(len(weights)):
			if(weights[j] <= i):
				if(table[i-weights[j]]+values[j] >= table[i]):
					table[i] = table[i-weights[j]]+values[j]
					selected[i].clear()
					selected[i].append(j+1)
					for val in selected[i-weights[j]]:
						selected[i].append(val)
	print(table[len(table)-1])
	print(selected[i])
			


weights = [5,4,2]
values= [10,4,3]
maxW = 9

knapsack(weights,values,maxW)
