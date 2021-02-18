/**
 * @param {string} s
 * @return {string}
 */
var reverseParentheses = function(s) {
    let stk = [];

    for(c of s){
        if(c!=')'){
            stk.push(c);
        }else{
            let store = [];

            while(stk[stk.length-1]!='('){
                store.push(stk.pop());
            }
            stk.pop();

            for(let i=0;i<store.length;i++){
                stk.splice(stk.length, 0, store[i]);
            }
        }
    }
    return stk.join('');
};