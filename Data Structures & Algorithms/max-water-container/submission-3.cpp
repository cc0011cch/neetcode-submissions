class Solution {
public:
    int maxArea(vector<int>& heights) {
        int marea{0};
        auto l{0};
        auto r{heights.size()-1};
        auto minHeight{(heights[l]<heights[r])? heights[l]: heights[r]};
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
