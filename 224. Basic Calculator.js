/**
 * @param {string} s
 * @return {number}
 */
var recursion = (s, cur)=>{
    let plus = 0, op = 1;

    while (cur[0]<s.length){
        let store = '';
        
        if (s[cur[0]] === '('){
            cur[0] += 1;
            plus += (op*recursion(s, cur));
        }else if (s[cur[0]] === ')'){
            return plus
        }else if (s[cur[0]]=='+'||s[cur[0]]=='-'){
            op = 44-s.charCodeAt(cur[0]);
        }
        
        while ( (cur[0]<s.length) && (!isNaN(parseInt(s[cur[0]]))) ){
            [store, cur[0]] = [store+s[cur[0]], cur[0]+1];
        }
        if (store){
            [plus, cur[0]] = [plus+op*parseInt(store, 10), cur[0]-1];
        }
        
        cur[0] += 1;
    }

    return plus;
}

var calculate = function(s) {
    return recursion(s, [0]);
};