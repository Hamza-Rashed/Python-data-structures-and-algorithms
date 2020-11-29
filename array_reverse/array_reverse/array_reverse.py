array = ['h' , 'a' , 2 , 5]
result = []
def reverseArray() :
    print(array)
    for i in reversed(array):
        result.append(i)
    print(result)


if __name__ == '__main__':

    reverseArray()