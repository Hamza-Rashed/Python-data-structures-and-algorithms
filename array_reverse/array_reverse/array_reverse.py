array = ['h' , 'a' , 2 , 5]
result = []
def reverseArray(arr) :
    for i in range(len(arr)-1,-1,-1):
        result.append(arr[i])
    print(result)

if __name__ == '__main__':

    reverseArray(array)
