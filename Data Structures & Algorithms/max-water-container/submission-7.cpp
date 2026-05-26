class Solution {
public:
    int maxArea(vector<int>& heights) {
        int marea{0};
        int l{0};
        int r{ static_cast<int>(heights.size())-1};
        int minHeight{(heights[l]<heights[r])? heights[l]: heights[r]};
        while (l<r){
            auto width{r-l}; 
            if (marea< minHeight*width ) marea=minHeight*width;
            if (minHeight == heights[l]) l++;
            else r--;
            minHeight= (heights[l]<heights[r])? heights[l]: heights[r];
        }
        return marea;
        
    }
};
