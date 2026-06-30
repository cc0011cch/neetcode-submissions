class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs :  return ""
        rlt=f'{len(strs):03d}'+f'{len(strs):03d}'.join(strs)
        return rlt

    def decode(self, s: str) -> List[str]:
        if s =="" : return list()
        rlt=s.split(s[:3])[1:]
        return rlt
