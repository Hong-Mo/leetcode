/**
 * @param {string} n
 * @return {number}
 */
var minPartitions = function(n) {
    let ans = 0;
    for(let c of n){
        ans = Math.max(ans, parseInt(c, 10));
    }
    return ans;
};