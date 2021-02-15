/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function(nums) {
    let [stk, ans] = [[], new Array(nums.length).fill(-1)];

    for(let i=0;i<2;i++){
        for(const [cur, cur_num] of Object.entries(nums)){
            while(stk.length>0 && cur_num>stk[stk.length-1][1]){
                let [past, past_num] = stk.pop();
                ans[past] = cur_num;
            }
            stk.push([cur, cur_num]);
        }
    }
    return ans;
};