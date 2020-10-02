import math
binarytree = [3, 9, 20, None, None, 15, 7]
length = len(binarytree)
print(length)
num_levels = math.log(7,2)
temp = int(num_levels)
#print(int(num_levels))
count = length
temp_list = []
result = []
print(2 ** temp)
for i in range(length):
	if  count != 2 ** temp:
		if binarytree[length-i-1] != None:
			temp_list.append(binarytree[length-i-1])
		count = count - 1
	else:
		if binarytree[length-i-1] != None:
			temp_list.append(binarytree[length-i-1])
		result.append(temp_list[::-1])
		temp_list.clear()
		count = count - 1
		temp = temp - 1
print(result)

