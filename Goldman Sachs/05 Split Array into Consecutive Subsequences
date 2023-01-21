class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if d.get(i) is None:
                d[i]=1
            else:
                d[i]+=1
        k={}
        for i in nums:
            if d[i]==0:
                continue
            if (k.get(i) is not None) and k[i]>0:
                k[i]-=1
                d[i]-=1
                if k.get(i+1) is None:
                    k[i+1]=1
                else:
                    k[i+1]+=1
            elif d[i]>0 and (d.get(i+1) is not None) and d[i+1]>0 and (d.get(i+2) is not None) and d[i+2]>0:
                d[i]-=1
                d[i+1]-=1
                d[i+2]-=1
                if k.get(i+3) is None:
                    k[i+3]=1
                else:
                    k[i+3]+=1    
            else:
                return False
        return True
                
 
 LEETCODE SUBMISSION LINK:https://leetcode.com/problems/split-array-into-consecutive-subsequences/solutions/3073609/split-array-into-consecutive-subsequences/               
