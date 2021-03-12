/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfArithmeticSlices = function(nums) {
    if(nums.length<3){
        return 0;
    }
    let [dif, last, cur, ans] = [nums[1]-nums[0], 0, 1, 0];

    while(cur<nums.length-1){
        while(cur<nums.length-1 && nums[cur+1]-nums[cur]==dif){
            cur += 1;
        }
        let l = (cur-last)+1;

        for(let i=3;i<l+1;i++){
            ans += (l-(i-1));
        }
        [last, cur] = [cur, cur+1];
        
        if(cur<nums.length-1){
            dif = nums[cur]-nums[cur-1];
        }
    }
    return ans;
};