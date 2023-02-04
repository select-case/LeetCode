class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int a = 0;
        int b = 0;
        for(auto it:nums){
            if(a==0){
                b = it;
            }
            if(b==it){
                a++;
            }
            else{
                a--;
            }
        }
        return b;
    }
};