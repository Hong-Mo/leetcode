/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    let stk = [];
    let accumulator = 0;
    let ans = 0;
    
    for (let i=0; i<s.length; i++){
        if (s[i]==='('){
            stk.push(0);
        }
        else if (stk.length>1){
            stk[stk.length-2] += (stk.pop()+2);
        }
        else if (stk.length==1){
            accumulator += (stk.pop()+2);   
        }
        else{
            ans = Math.max(ans, accumulator);
            accumulator = 0
        }
    }
    stk.push(accumulator);
    stk.push(ans);
    
    return Math.max(...stk);
};