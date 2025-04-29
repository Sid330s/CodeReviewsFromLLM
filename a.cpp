class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        /*
                1 2 3 4 3


                1. 2
                2. 3
                3  4
                4. -1
                3. 

                ---------------------
                travel reverse , start from largest element

                -1

                4,3

                1,2,3,4,3

                2,3,4,-1,4

        */

        int n = nums.size();
        vector<int> res(n, -1);
        stack<int> st;


        int maxIdx = 0;
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[maxIdx]) {
                maxIdx = i;
            }
        }

        st.push(nums[maxIdx]);


        for (int k = 1; k <= n; ++k) {
            int i = (maxIdx - k + n) % n; // reverse circular index
            while (!st.empty() && st.top() <= nums[i]) {
                st.pop();
            }
            if (!st.empty()) {
                res[i] = st.top();
            }
            st.push(nums[i]);
        }

        // max element itself has no next greater, leave res[maxIdx] as -1
        return res;

    }
};