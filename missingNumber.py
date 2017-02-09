def find_missing(a,b):
  total = a + b
  if total == 0 or a == b:
    return 0
    
  for i in a:
      if i not in b:
        return i
  for j in b:
          if j not in a:
            return j
            return 0
    
    