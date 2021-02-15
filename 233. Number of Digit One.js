/**
 * @param {number} n
 * @return {number}
 */
var countDigitOne = function(n) {
    if (n<0){
        return 0;
    }
    let ans = 0, bound = 10, base = 1;
    let num = [base];

    while (n>=bound*10){
        base = base*10 + bound;
        bound *= 10;
        num.push(base);
    }
    while (bound>1){
        let quo = Math.floor(n/bound);
        n %= bound, ans += (quo*num.pop());

        if (quo>1){
            ans += bound;
        }else if(quo==1){
            ans += (n+1);
        }
        bound /= 10;
    }
    if (n>0){
        ans += 1;
    }
    return ans;
};