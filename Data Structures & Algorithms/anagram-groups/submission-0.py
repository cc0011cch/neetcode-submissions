class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs:
            a_count=[0]*26
            for c in s:
                a_count[ord(c)-97]=a_count[ord(c)-97]+1
            result[tuple(a_count)].append(s)
        return list(result.values())
        