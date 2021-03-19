/**
 * @param {string} s
 * @return {string}
 */
 var reverseWords = function(s) {
    let [cur, stk, ans] = [0, [], ''];

    while(cur<s.length){
        let word = '';

        while(cur<s.length && s[cur]==' '){
            cur += 1;
        }
        while(cur<s.length && s[cur]!=' '){
            word += s[cur];
            cur += 1;
        }
        if(word.length>0){
            stk.push(word);
        }
    }
    while(stk.length>0){
        ans += stk.pop()+' ';
    }
    return ans.slice(0, -1);
};