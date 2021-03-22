/**
 * @param {string} s
 * @return {number}
 */
 var maxScore = function(s) {
    let ans = score = 0;

    for(let c of s){
        if(c=='1'){
            score += 1;
        }
    }
    for(let i=0;i<s.length-1;i++){
        if(s[i]=='1'){
            score -= 1;
        }else{
            score += 1;
        }
        ans = Math.max(ans, score);
    }
    return ans;
};