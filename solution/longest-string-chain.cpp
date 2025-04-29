class Solution {
public:
    int longestStrChain(vector<string>& words) {

        sort(words.begin(), words.end(), [](const string &a, const string &b) {
            return a.length() < b.length();
        });

        unordered_map<string, int> dp;
        int maxLen = 1;

        for (const string &word : words) {
            int best = 0;

            for (int i = 0; i < word.size(); ++i) {
                string prev = word.substr(0, i) + word.substr(i + 1);
                best = max(best, dp[prev] + 1);
            }

            dp[word] = best;
            maxLen = max(maxLen, best);
        }

        return maxLen;
    }
};