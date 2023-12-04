class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minlen=len(strs[0])
        minnumber=strs[0]
        for i in strs: #find the shortest substring
            if len(i)<minlen:
                minlen=len(i)
                minnumber=i
        index=minlen
        for i in strs:
            if i==minnumber:
                continue
            for j in range(minlen):#dont need to care after the shortest string
                if i[j] !=minnumber[j]:
                    if j<index:
                        index=j
                    break
        print(minnumber[:index])    
strs = ["dog","racecar","car"]
solution=Solution()
solution.longestCommonPrefix(strs)