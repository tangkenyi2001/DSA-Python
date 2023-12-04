class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result=-1
        check=False
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2] and int(num[i])>result/111:
                check=True
                result=int(num[i])*111
        if (check==False):
            result=""
        if (result==0):
            result="000"
            
        return str(result)
                
            


num="42352338"
Solution1=Solution()
x=Solution1.largestGoodInteger(num)
print(x)
