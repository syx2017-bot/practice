def CheckPermutation(self, s1: str, s2: str) -> bool:
        dict1=dict()
        dict2=dict()
        
        
        for i in s1:
            dict1[i]=s1.count(i)
        for j in s2:
            dict2[j]=s2.count(j)
        return dict1==dict2
