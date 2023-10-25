#
                                    #[0 , 1, 2,3, 4, 5]
def Insertion_sort(lst):            #[12,31,25,8,32,17] 
   for i in range(1,len(lst)):      # i =2
      temp=lst[i]                   #temp=25
      j=i-1                          #j=1
      while j>=0 and temp < lst[j]:  #25 < 31
         lst[j+1] = lst[j]           #25 = 31
         j-=1                        # j= 0

      lst[j+1]=temp                  # lst[1] = 25
   return lst
print(Insertion_sort([12,31,25,8,32,17]))
 
