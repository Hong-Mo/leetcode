/**
 * @param {string} s
 * @return {string[]}
 */
var printVertically = function(s) {
    let [ans, word, pre] = [[], s.split(' '), 1];
    
    while(pre){
        let ins = '';
        pre = 0

        for(let i=word.length-1;i>-1;i--){
            if(!(pre || word[i])){
                continue;
            }else if(word[i]){
                [ins, word[i]] = [word[i][0]+ins, word[i].slice(1)];
            }else{
                ins = ' '+ins;
            }
            pre = 1;
        }
        ans.push(ins);
    }
    ans.pop();

    return ans;
};