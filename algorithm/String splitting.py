#use the split function to split the string
def reverseWords(self, s: str) -> str:
        st=''
        for i in s.split():
            st+=i[::-1]+' '
        return st[:-1]
