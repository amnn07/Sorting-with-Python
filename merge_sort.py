def merge_sort(arr):
   if len(arr)>1:
      left_arr=arr[:len(arr)//2]
      right_arr=arr[len(arr)//2:]
      merge_sort(left_arr)
      merge_sort(right_arr)
      low=0
      high=0
      index=0
      while low<len(left_arr) and high<len(right_arr):
         if left_arr[low]<right_arr[high]:
            arr[index]=left_arr[low]
            low+=1
         else:
            arr[index]=right_arr[high]
            high+=1
         index+=1
      while low<len(left_arr):
         arr[index]=left_arr[low]
         low+=1
         index+=1
      while high<len(right_arr):
         arr[index]=right_arr[high]
         high+=1
         index+=1
arr=[54,6,5,6,4,7,8,5,1,1,2,3,6,5,4,778,95,6,7,89]
merge_sort(arr)
print(arr)
