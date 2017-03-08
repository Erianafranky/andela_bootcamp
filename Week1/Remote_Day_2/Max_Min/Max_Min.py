def find_max_min(n):
  
  min_num = min(n)
  max_num = max(n)
  
  if min_num == max_num:
    return [len(n)]
  else:
    return [min_num,max_num]
     
    
  