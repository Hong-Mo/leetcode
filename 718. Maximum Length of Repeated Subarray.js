/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number}
 */
var findLength = function(A, B) {
    let [ans, dp] = [0, []];
    for(let i=0;i<A.length+1;i++)
        dp.push(new Array(B.length+1).fill(0));
    
        for(let i=1;i<B.length+1;i++){
            for(let j=1;j<A.length+1;j++){
                if(B[i-1]==A[j-1]){
                    let cur = dp[i-1][j-1]+1;
                    [dp[i][j], ans] = [cur, Math.max(ans, cur)];
                }
            }
        }
    return ans;
};