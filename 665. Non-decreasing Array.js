/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function(nums) {
    let cnt = 0;
    
    for(let i=0;i<nums.length-1;i++){
        if(nums[i]>nums[i+1]){
            if(cnt==1 || ((i+2<nums.length && nums[i]>nums[i+2]) &&
            (i-1>=0 && nums[i-1]>nums[i+1]))){
                return false;
            }
            cnt += 1;
        }
    }
    return true;
};