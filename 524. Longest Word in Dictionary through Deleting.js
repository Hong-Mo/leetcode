/**
 * @param {string} s
 * @param {string[]} d
 * @return {string}
 */
var findLongestWord = function(s, d) {
    let [word, ans] = [d.slice(0), ''];

    for(let i=0;i<d.length;i++){
        d[i] = d[i].split('');
    }
    for(const c of s){
        for([i, check] of Object.entries(d)){
            if(check.length>0 && check[0]==c){
                check.splice(0, 1);

                if (check.length==0 && (word[i].length>ans.length
                   ||(word[i].length==ans.length && word[i]<ans))){
                    ans = word[i];
                }
            }
        }
    }
    return ans;
};