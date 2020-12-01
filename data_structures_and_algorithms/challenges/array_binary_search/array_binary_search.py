def BinarySearch(arr_num, add_val):
      left = 0 # start from 0
      right = (len(arr_num)-1) # last index from the list

      while left <= right:
          middle = left + (right) + 1 // 2
          if add_val == arr_num[middle]:
              return middle
          elif add_val < arr_num[middle]:
              right = middle - 1
          else:
              left = middle + 1
      return -1
