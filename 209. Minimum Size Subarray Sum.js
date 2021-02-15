/**
 * @param {number} s
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(s, nums) {
    let [l, r, acc, ans] = [0, -1, 0, nums.length+1];

    while (r<nums.length-1){
        while(acc<s && r<nums.length-1){
            r += 1;
            acc += nums[r];
        }
        while(acc>=s){
            [acc, ans] = [acc-nums[l], Math.min(ans, r-l+1)];
            l += 1;
        }
    }
    if (ans==nums.length+1){
        return 0;
    }
    return ans;
};