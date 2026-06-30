class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs : 
            return ""
        rlt=f'{len(strs):03d}'+f'{len(strs):03d}'.join(strs)
        print(rlt)
        return rlt

    def decode(self, s: str) -> List[str]:
        if s =="" : return list()
        rlt=s.split(s[:3])[1:]
#        rlt=[]
#        delimit=3
#        idx=0;
#        while idx<len(s):
#            str_len= int(s[idx:idx+delimit])
#            word=s[idx+delimit:idx+delimit+str_len]
#            rlt.append(word)
#            idx=idx+delimit+str_len

        return rlt
