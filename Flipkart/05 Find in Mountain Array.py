# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        low = 0
        high = mountain_arr.length()
        peak = -1
        
        while (low < high - 1):
            mid = (low + high) // 2
            midVal = mountain_arr.get(mid)
            leftMid = mountain_arr.get(mid - 1)
            rightMid = mountain_arr.get(mid + 1)

            if (midVal > leftMid and midVal > rightMid):
                peak = mid
                break
            elif (midVal > leftMid and midVal < rightMid):
                low = mid 
            else:
                high = mid
        
        low = 0
        high = peak
        while (low <= high):
            mid = (low + high) // 2
            midVal = mountain_arr.get(mid)
            
            if midVal == target:
                return mid
            elif midVal < target:
                low = mid + 1
            else:
                high = mid - 1
                
        low = peak
        high = mountain_arr.length() - 1
        while (low <= high):
            mid = (low + high) // 2
            print(low, mid, high)
            midVal = mountain_arr.get(mid)
            
            if midVal == target:
                return mid
            elif midVal < target:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1
        
