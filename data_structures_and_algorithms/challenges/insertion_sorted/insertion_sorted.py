def InsertionSort(arr):
    first = 1

    for first in range(len(arr)):
        second = first - 1
        finall = arr[first]

        while second >= 0 and finall < arr[second]:
            arr[second + 1] = arr[second]
            second -= 1

        arr[second + 1] = finall

    return arr

if __name__ == '__main__':
    print(InsertionSort([8,4,23,42,16,15]))