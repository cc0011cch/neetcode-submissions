class Solution {
public:
    int maxArea(vector<int>& heights) {
        int marea{0};
        int l{0};
        int r{ static_cast<int>(heights.size())-1};
        
        while (l<r){
            int width{r-l};
            int minHeight{(heights[l]<heights[r])? heights[l]: heights[r]}; 
            if (marea< minHeight*width ) marea=minHeight*width;
            if (heights[l]< heights[r]) l++;
            else r--;
        }
        return marea;
        
    }
};
