def find_missing(arr1,arr2):
    total = arr1 + arr2
    if total == 0 or arr1 == arr2:
      return 0
    
    for i in arr1:
        if i not in arr2:
            return i
    for j in arr2:
      if j not in arr1:
        return j
    return 0