class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max=nums[0],current=0;
        for(auto it:nums){
            current+=it;
            if(current>max){
                max=current;
            }
            if(current<=0){
                current = 0;
            }
        }
        return max;
    }
};