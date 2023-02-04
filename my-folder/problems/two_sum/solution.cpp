bool comp(pair<int,int> one,pair<int,int> two){
    if(one.first>two.first){
        return false;
    }
    if(one.first == two.first && one.second>two.second){
        return false;
    }
    return true;
}

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // vector<pair<int,int>> v1;
        pair<int,int> v[nums.size()];
        for(int i = 0;i < nums.size();i++){
            v[i] = {nums[i],i};
        }
        sort(v,v+nums.size(),comp);
        for (auto it:v){
            cout<<it.first<<" "<<it.second<<endl;
        }
        int k = nums.size();
        int i = 0,j = nums.size()-1;
        int sum;
        while(i < j){
            sum = v[i].first+v[j].first;
            if(sum == target && i !=j ){
                vector<int> v1 = {v[i].second,v[j].second};
                return(v1);
            }
            else if(sum <= target){
                i++;
            }
            else{
                j--;
            }
        }

    vector<int> v2 = {1};
    return(v2);
    }
};
