class Solution:

    def encode(self, strs: List[str]) -> str:
        rlt=""
        for s in strs:
            rlt+=(f'{len(s):03d}'+s)
        print(rlt)
        return rlt

    def decode(self, s: str) -> List[str]:
        rlt=[]
        delimit=3
        idx=0;
        while idx<len(s):
            str_len= int(s[idx:idx+delimit])
            word=s[idx+delimit:idx+delimit+str_len]
            rlt.append(word)
            idx=idx+delimit+str_len

        return rlt
