/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let stk = [nums], ans = [];

    while (stk.length){
        let cur = stk.pop();
        let l=0, r=cur.length-1;

        while (l<r){
            let mid = Math.floor((l+r)/2);

            if (cur[mid]<cur[r]){
                r = mid;
            }else if (cur[mid]>cur[r]){
                l = mid+1;
            }else{
                stk.push(cur.slice(l, mid));
                stk.push(cur.slice(mid+1, r+1))
                break
            }
        }

        if (r===l && cur.length){
            ans.push(cur[l]);
        }
    }
    return Math.min(...ans);
};