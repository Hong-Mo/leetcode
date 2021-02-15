/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numberOfSubarrays = function(nums, k) {
    for(let i=0;i<nums.length;i++)
        nums[i] %= 2;
    
    let odd = ans = 0;
    let com_num= [];
    for(let i=0;i<nums.length;i++)
        com_num.push([0, 0]);
    let [left, right, l_o, r_o] = [0, nums.length-1, -1, nums.length];

    while(left<nums.length){
        if(nums[left]==1)
            [com_num[left][0], l_o] = [left-l_o, left];
        
        if (nums[right]==1)
            [com_num[right][1], r_o] = [r_o-right, right];
        
        [left, right] = [left+1, right-1];
    }
    left = right = 0;

    while(right<nums.length){
        while(right<nums.length && odd!=k)
            [odd, right] = [odd+nums[right], right+1];
        
        while(odd==k && nums[left]!=1)
            left += 1;

        ans = ans+com_num[left][0]*com_num[right-1][1];
        [left, odd] = [left+1, odd-1];
    }
    return ans;
};