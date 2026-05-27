class Solution {
public:
    bool isValid(string s) {
        if (s.length() % 2 != 0) return false;

        // 1. 先建立一個底層的 vector，並直接預留足夠的空間
        vector<char> raw_vector;
        raw_vector.reserve(s.length() / 2); 

        // 2. 用這個已經優化好的 vector 來初始化 stack
        // 這時 st.push(')') 就不會觸發任何「動態記憶體重配置」
        stack<char, vector<char>> st(move(raw_vector)); 

        for (char c : s) {
            switch (c) {
                case '(': st.push(')'); break;
                case '[': st.push(']'); break;
                case '{': st.push('}'); break;
                default:
                    if (st.empty() || c != st.top()) return false;
                    st.pop();
                    break;
            }
        }
        return st.empty();
    }
};