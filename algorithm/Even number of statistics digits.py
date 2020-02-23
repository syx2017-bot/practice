def findNumbers(nums):
        listr=[]
        for i in nums:
            if (len(str(i))%2==0):
                listr.append(i)
            else:
                continue
        return len(listr)
