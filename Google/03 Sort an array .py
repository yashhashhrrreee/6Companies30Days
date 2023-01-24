def merge2array(arr1,arr2):
        i = 0
        j = 0
        arr3 = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                arr3.append(arr1[i])
                i += 1
            else:
                arr3.append(arr2[j])
                j += 1
        if i == len(arr1) and j != len(arr2):
            for k in range(j,len(arr2)):
                arr3.append(arr2[k])
        elif j == len(arr2) and i != len(arr1):
            for k in range(i,len(arr1)):
                arr3.append(arr1[k])
        return arr3

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        return merge2array(merge_sort(arr[:int(len(arr)/2)]),merge_sort(arr[int(len(arr)/2):]))
        
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return merge_sort(nums)
    
