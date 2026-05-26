class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea=0;
        lidx=0;
        ridx=len(heights)-1
        minheight= min(heights[lidx], heights[ridx])
        while lidx<ridx:
            width=ridx-lidx
            print([minheight, width, minheight*width])
            maxarea = max(maxarea, minheight*width)
            if minheight == heights[lidx]:
                lidx+=1
            else: ridx-=1
            minheight= min(heights[lidx], heights[ridx])
        return maxarea

        