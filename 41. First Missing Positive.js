/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    let i=0;

    while (i<nums.length){
        let cur = nums[i];

        while ((cur>0 && cur<=nums.length) 
              && cur!==nums[cur-1] && cur-1!==i){
            [nums[cur-1], cur] = [cur, nums[cur-1]];
        }
        nums[i] = cur;
        i += 1;
    }
    for (let i=0;i<nums.length;i++){
        if (nums[i]!=i+1){
            return i+1;
        }
    }
    return nums.length+1;
};