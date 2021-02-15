/**
 * @param {string} S
 * @return {string}
 */
var reorganizeString = function(S) {
    let [ans, count] = ['', new Array(26).fill(0)];

    for(let i=0;i<S.length;i++){
        count[S.charCodeAt(i)-97]+=1;
    }
    let pre = count.indexOf(Math.max(...count));
    [ans, count[pre]] = [ans+String.fromCharCode(pre+97), count[pre]-1];

    for(let i=0;i<S.length-1;i++){
        let s = count[pre];
        count[pre] = 0;
        let cur = count.indexOf(Math.max(...count));

        if(count[cur]==0){
            return '';
        }
        [ans, count[cur], count[pre]] = [ans+String.fromCharCode(cur+97), count[cur]-1, s];
        pre = cur;
    }
    return ans;
};