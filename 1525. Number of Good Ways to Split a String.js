/**
 * @param {string} s
 * @return {number}
 */
var numSplits = function(s) {
    let left = right = ans = 0;
    let [l_count, r_count] = [new Object(), new Object()];

    for(c of s){
        if(!Object.keys(r_count).includes(c)){
            r_count[c] = 1;
        }else{
            r_count[c] += 1;
        }
    }
    for(c of s){
        if(!Object.keys(l_count).includes(c)){
            l_count[c] = 1;
        }else{
            l_count[c] += 1;
        }
        r_count[c] -= 1;
        
        if(r_count[c]==0){
            delete r_count[c];
        }
        if(Object.keys(l_count).length==Object.keys(r_count).length){
            ans += 1;
        }
    }
    return ans;
};