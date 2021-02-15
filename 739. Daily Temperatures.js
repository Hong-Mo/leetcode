/**
 * @param {number[]} T
 * @return {number[]}
 */
var dailyTemperatures = function(T) {
    let [stk, ans] = [[], new Array(T.length)];
    for(let cur=0;cur<T.length;cur++){
        ans[cur] = 0;

        while(stk.length!=0 && T[cur]>stk.slice(-1)[0][1]){
            let [p, p_temp] = stk.pop();
            ans[p] = cur-p;
        }
        stk.push([cur, T[cur]]);
    }
    return ans;
};