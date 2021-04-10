def string_match(a, b):
  """
  Assumes list or string. 
  Returns the index and same elements as well as the number of times same substring appears in the same index. 
  For example: a = "acbeda", b = "acxeda" returns 3 because "ac" "ed" "da" 
  appears to be both same and in the same index.   
  """
  counter = 0
  dic = {}
  if len(a) < 2 or len(b) < 2:
    return None
  for i in range(0, len(a)-1):
    for c in range(0, len(b)-1):
      if a[i:i+2] == b[c:c+2] and i == c:
        counter += 1 
        dic[str(i) + '-' + str(i+2)] = a[i:i+2]
  return counter, dic

#x = string_match([1,2,3,6,78], [1,2,4,6,78,8,9,10,21])
#print(x)
