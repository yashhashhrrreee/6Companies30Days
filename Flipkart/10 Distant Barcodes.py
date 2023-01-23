class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        s=set(barcodes)
        x=len(s)
        if(x==1):
            return barcodes
        barcodes.sort()
        q=mode(barcodes)
        p=0
        x1=0
        while(p<len(barcodes)):
            if(barcodes[p]==q):
                del(barcodes[p])
                x1=x1+1
                continue  
            p=p+1       
        l2=len(barcodes)
        l1=[0]*x1*x
        z=0
        a=0
        i=0
        while(a<l2 and i<len(l1)):
            l1[z+i]=q
            i=i+x
        z=1
        while(z<x):
            i=0
            while(a<l2 and i<len(l1)):
                l1[z+i]=barcodes[a]
                a=a+1
                i=i+x
            z=z+1
        i=0
        while(i<len(l1)):
            if(l1[i]==0):
                del(l1[i])
                continue
            i=i+1
        return l1
