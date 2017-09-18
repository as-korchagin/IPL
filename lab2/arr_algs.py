def array_min(array):
    min_value = array[0]
    for i in range(1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
    return min_value


print(array_min(list(int(i) for i in input().split(','))))