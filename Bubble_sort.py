def Bubble_Sort(lst):
   for i in range(0,len(lst)):
      for j in range(i+1,len(lst)):
         if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
   return lst
print(Bubble_Sort([13,32,26,10,35]))
