array = [2, 1, 1, 2, 3 ,5]
min_1 = array[0]
min_2 = array[1]
for i in array:
    if i < min_1:
        min_2 = min_1
        min_1 = i 
    elif min_1 == min_2 != i:
        min_2 = i
    else:
        if min_1 > i < min_2:
            min_2 = i
if min_1 == min_2:
    print(f'Массив состоит из одинаковых элементов')
print(min_1, min_2)
