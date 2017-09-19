def array_min(array):
    min_value = array[0]
    for i in range(1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
    return min_value

	
def array_average(array):
	sum = 0
	for i in array:
		sum += i
	return sum / len(array)
	
	
input_array = list(int(i) for i in input().split(','))
print(array_min(input_array))
print(array_average(input_array))
