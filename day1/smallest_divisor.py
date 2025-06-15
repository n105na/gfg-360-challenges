import math
class Solution:
    def calculate_sum(self,arr,d):
        total=0
        for num in arr:
            total+=math.ceil(num/d)
        return total
    def smallestDivisor(self, arr, k):
        low=1 
        high=max(arr)
        result = high
        while low <= high :
            mid = (low+high)//2
            som = self.calculate_sum(arr,mid)
            if som > k :
               low = mid+1
            else:
                result = mid
                high = mid - 1
            
        return result
        
    
        
        
