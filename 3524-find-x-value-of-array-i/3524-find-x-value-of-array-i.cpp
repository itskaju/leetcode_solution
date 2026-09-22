class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        int n = nums.size();

        vector<int> A(n , 0);

        for(int i = 0; i < n; ++i) 
           A[i] = nums[i] % k;

        vector<vector<int>> dp(n + 1 , vector<int>(k , 0));

        dp[0][A[0]]++;

        for(int i = 1; i < n; ++i) {
            for(int j = 0; j < k; ++j) 
                dp[i][(j * A[i])%k] += dp[i - 1][j];

            dp[i][A[i]]++;    
        }        


         vector<long long> ans(k , 0);

         for(int i = 0; i < n; ++i) 
            for(int j = 0; j < k; ++j) 
                ans[j] += dp[i][j];

          return ans;               
    }
};