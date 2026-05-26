class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedStr;
        for(auto word:strs)
            encodedStr+= std::format("{:03d}",word.size())+word;
        return encodedStr;
    }

    vector<string> decode(string s) {
        vector<string> decodedStr;
        int idx{0};
        int delimiter{3};
        while (idx< s.size()){
            int w_len=stoi(s.substr(idx,delimiter));
            idx+=delimiter;
            string word=s.substr(idx, w_len);
            decodedStr.push_back(word);
            idx+=w_len;
        }
        return decodedStr;
    }
};
