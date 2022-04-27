
def merge_sort(array):  # sorting
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def binary_search(array, element):
    try:
        element = int(element)
    except ValueError:
        return "Введите число!"
    if element not in array:
        return "Число выходит за пределы заданного диапазона!"

    middle = len(array) // 2
    if array[middle] == element:
        try:
            return array[middle - 1], array[middle + 1]
        except IndexError:
            return array[middle - 1], array[middle]
    elif element > array[middle]:
        return binary_search(array[middle:], element)
    else:
        return binary_search(array[:middle + 1], element)

num = '20 17 21 57 2 31 8 10 11 15 14 13 12 16 19 18 44 27 39 26'
array_ = list(map(int, num.split()))
point = int(input('Введите любое число от 1 до 50: '))
print(merge_sort(array_))
print(binary_search(array_, point))