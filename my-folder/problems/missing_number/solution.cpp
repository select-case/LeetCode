class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sum = 0;
        for(int i=0;i<nums.size();i++){
            sum+=nums[i];
        }
        cout<<sum<<endl<<nums.size()<<endl;
        int k = nums.size();
        return (k*(k+1)/2)-sum;
        return 0;
    }
};
