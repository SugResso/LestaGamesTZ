# Я выбрал алгоритм быстрой сортировки, у которого O(n*log*n). Такое же время у сортировки слиянием, 
# но вот константа у быстрой сортировки меньше. Если смотреть на практику, то быстрая сортировка выигрывает 
# у сортировки слиянием, только потому что средних случаев больше, чем худших в которых быстрая сортировка
# была бы хуже.


def quicksort(array):
    if len(array) < 2:
	return array
    else:
	pivot = array[0]
	less = [i for i in array[1:] if i < pivot]
	greater = [i for i in array[1:] if i > pivot]
	return quicksort(less) + [pivot] + quicksort(greater)


def test_quicksort():
    print(quicksort([4, 1, 2, 3]))
    print(quicksort([1, 2, 3, 4]))
    print(quicksort([3]))
    print(quicksort([10331, 1231222, 55011]))
    print("Введите список значений, чтобы отсортировать их: ", end="")
    print(quicksort(list(map(int, input().split()))))



if __name__ == '__main__':
    test_quicksort()
