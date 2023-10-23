'''def Selection_Sort(lst):
   for i in range(0,len(lst)):
      small=i
      for j in range(i+i,len(lst)):
         if lst[small]>lst[j]:
            small=j
      lst[i],lst[small]=lst[small],lst[i]
   return lst
print(Selection_Sort([8,12,3,14,9]))
'''
def selection(lst):
    for i in range(0,len(lst)):
        small=i
        for j in range(i+i,len(lst)):
            if lst[small]>lst[j]:
                small=j
        lst[i],lst[small]=lst[small],lst[i]
    return lst
print(selection([8,12,3,14,9]))
