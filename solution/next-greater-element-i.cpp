class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int n = nums2.size();
        stack<int> st;
        unordered_map<int,int> nextGreater;

        int maxIdx = n-1;
        nextGreater[nums2[maxIdx]] = -1;

        st.push(nums2[maxIdx]);

        for (int k = 1; k <= n-1; k++) {
            int i = (maxIdx - k + n) % n;
            while (!st.empty() && st.top() <= nums2[i]) {
                st.pop();
            }
            if (!st.empty()) {
                nextGreater[nums2[i]]=st.top();
            }
            else{
                nextGreater[nums2[i]]=-1;
            }
            st.push(nums2[i]);
        }

        for(int i=0;i<nums1.size();i++){
            nums1[i] = nextGreater[nums1[i]];
        }


        return nums1;

    }
};