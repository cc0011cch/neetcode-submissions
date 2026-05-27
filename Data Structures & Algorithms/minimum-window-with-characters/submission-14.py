class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap=defaultdict(int)
        smap=defaultdict(int)
        l=0
        formed=0
        ans=[float('inf'), None,None]
        for i in t:
            tmap[i]+=1
        required =len(tmap)
        
        for r in range(len(s)):

            if s[r] in tmap:
                smap[s[r]]+=1
            if s[r] in tmap and smap[s[r]]==tmap[s[r]]:
                formed+=1
            print([s[r], smap[s[r]], formed, required])
            while l<=r and formed==required:
                if r-l+1<ans[0]:
                    ans =[r-l+1,l,r]
                    print(ans)
                if s[l] in tmap:
                    smap[s[l]]-=1
                if s[l] in tmap and smap[s[l]]<tmap[s[l]]:
                    formed-=1
                l+=1
        
                

        return '' if ans[0]==float('inf') else s[ans[1]:ans[2]+1]