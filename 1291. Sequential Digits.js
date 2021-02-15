/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function(low, high) {
    let [cur, digit, s, ans] = [1, low.toString().length, low.toString(), []];

    if (s[0].charCodeAt()+digit-1<=57){
        [digit, cur] = [digit-1, parseInt(s[0])]
    }
    let [ini, tail, increment] = ['1', cur+1, 1];

    for (let i=0;i<digit;i++){
        [cur, increment] = [cur*10+tail, increment*10+1];
        ini = ini+(String.fromCharCode(ini[ini.length-1].charCodeAt()+1));
        tail += 1
    }

    while(cur<=high){
        if (cur>=low){
            ans.push(cur);
        }
        s = cur.toString();

        if(s[s.length-1].charCodeAt()==57){
            if (s[0].charCodeAt()==49){
                break
            }
            ini = ini+(String.fromCharCode(ini[ini.length-1].charCodeAt()+1));
            [cur, increment] = [parseInt(ini), increment*10+1];
        }else{
            cur += increment;
        }
    }
    return ans;
};