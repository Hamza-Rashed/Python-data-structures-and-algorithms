def insertShiftArray(arr,num):
    result = []
    for item in range(len(arr)):
        if arr[item] < num:
           result.append(arr[item])#done
        elif arr[item] > num and arr[item-1] < num:
            result.append(num)
        else:
            result.append(arr[item-1])
    result.append(arr[len(arr)-1])         
    return result